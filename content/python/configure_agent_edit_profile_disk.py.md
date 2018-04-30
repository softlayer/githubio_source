---
title: "configure_agent_edit_profile_disk.py"
description: "configure_agent_edit_profile_disk.py"
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
Edit the configuration for the "Disk Profile" section
of a monitoring agent.

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
ipAddres = "5.153.59.197"

configuration = {
    'Disk Path': "c:/",
    'Description': "file system c:/",
    'Graph Disk Usage': "TRUE",
    'Graph Disk Usage as Percentage': "TRUE",
    'Disk Usage Error Alarm': "TRUE",
    'Usage Error Alarm Threshold': "95",
    'Disk Usage Warning Alarm': "TRUE",
    'Disk Usage Warning Threshold': "90",
}

# The agent's name we will configure.
agentName = 'Cpu, Disk, and Memory Monitoring Agent'

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']
hardwareService = client['SoftLayer_Hardware_Server']
monitoringService = client['SoftLayer_Monitoring_Agent']

# Getting the monitoring agents installed in the server or VSI.
try:
    objectMask = 'mask[monitoringAgents[configurationValues[definition]]]'
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

# Getting the profile id to edit.
if 'Disk Path' in configuration:
    profileId = [value['profileId'] for value in agent['configurationValues']
                 if value['definition']['name'] == 'Disk Path' and
                 value['value'].strip().upper() == configuration['Disk Path'].strip().upper()]
    profileId = profileId[0]
else:
    print("It is required an Disk Path value in the configuration.")
    exit(1)

# Creating an SoftLayer_Monitoring_Agent_Configuration_Value skeleton
# which contains the configuration for the agent.
configurationValues = []
for item in configuration.keys():
    itemFound = False
    for value in agent['configurationValues']:
        if value['definition']['name'].strip().upper() == item.strip().upper() and value['profileId'] == profileId:
            itemFound = True
            configurationValue = value
            configurationValue['value'] = configuration[item].strip().upper()
            configurationValues.append(configurationValue)
            break
    if not itemFound:
        print("The configuration: " + item + " is not available for the agent.")

# Calling the SoftLayer_Monitoring_Agent::applyConfigurationValues method
# to apply the changes in the agent.
# Note: In case there is no changes in the agent configuration the method
# will return error.
try:
    result = monitoringService.addConfigurationProfile(configurationValues, id=agent['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to apply the configuration in the monitoring agent: faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
