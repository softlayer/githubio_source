---
title: "configure_agent_creating_new_profile_disk.py"
description: "configure_agent_creating_new_profile_disk.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Monitoring_Agent_Configuration_Value"
tags:
    - "monitoring"
---


```
"""
Create a new 'Disk Profile' configuration for the 'Cpu, Disk, and Memory Monitoring Agent' agent.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# The IP address of the server or VSI to configure.
ipAddres = "23.246.195.66"

configuration = {
    'Disk Path': "c:/",
    'Description': "file system c:/",
    'Graph Disk Usage': "TRUE",
    'Graph Disk Usage as Percentage': "TRUE",
    'Disk Usage Error Alarm': "TRUE",
    'Usage Error Alarm Threshold': "90",
    'Disk Usage Warning Alarm': "TRUE",
    'Disk Usage Warning Threshold': "90",
}

# The agent's name we wish to configure.
agentName = 'Cpu, Disk, and Memory Monitoring Agent'
# The agent's section we wish to change
sectionName = "Disk Profile"

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']
hardwareService = client['SoftLayer_Hardware_Server']
monitoringService = client['SoftLayer_Monitoring_Agent']

# Getting the monitoring agents installed in the server or VSI.
try:
    objectMask = 'mask[monitoringAgents[configurationTemplate[configurationSections[subSections[definitions]]]]]'
    server = vsiService.findByIpAddress(ipAddres, mask=objectMask)
    if not 'id' in server:
        server = hardwareService.findByIpAddress(ipAddres, mask=objectMask)
        if not 'id' in server:
            print("There is no a Server or VSI with the IP address: " + ipAddres)
            exit(1)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the server: faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

# Getting the agent to configure.
agents = [agent for agent in server['monitoringAgents'] if agent['name'] == agentName]
if len(agents) == 0:
    print("Unable to find the agent: " + agentName)
    exit(1)
agent = agents[0]

# Getting the section to configure
sections = [section for section in agent['configurationTemplate']['configurationSections'] if section['name'] == sectionName]
if len(sections) == 0:
    print("Unable to find the section: " + sectionName)
    exit(1)
section = sections[0]


# Creating the configuration for the agent.
configurationValues = []
for item in configuration.keys():
    itemConfigured = False
    for subsection in section['subSections']:
        for definition in subsection['definitions']:
            if definition['name'].strip().upper() == item.strip().upper():
                configurationValue = {}
                itemConfigured = True
                configurationValue['configurationDefinitionId'] = definition['id']
                configurationValue['agentId'] = agent['id']
                configurationValue['value'] = configuration[item]
                configurationValues.append(configurationValue)
        if itemConfigured:
            break
    if not itemConfigured:
        print ("Unable to configure: " + item + " the configuration name was not found.")

# Calling the SoftLayer_Monitoring_Agent::applyConfigurationValues method
# to apply the changes in the agent.
try:
    result = monitoringService.addConfigurationProfile(configurationValues, id=agent['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to apply the configuration in the monitoring agent: faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
