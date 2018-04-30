---
title: "configure_agent_memory.py"
description: "configure_agent_memory.py"
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
Configure the section 'Memory' from the 'Cpu, Disk, and Memory Monitoring Agent' agent.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# The IP address of the server or VSI to configure.
ipAddres = "5.153.59.197"

configuration = {
    "Graph Memory Usage": "FALSE",
    "Graph Memory Usage as Percentage": "TRUE",
    "Graph Physical Memory Usage": "FALSE",
    "Graph Physical Memory Usage as Percentage": "TRUE",
    "Graph Swap Memory Usage": "FALSE",
    "Graph Swap Memory Usage as Percentage": "TRUE",
    "Graph System Paging in Kb/s": "TRUE",
    "Graph System Paging in Pg/s": "FALSE",
    "Total Memory Usage Error Alarm": "FALSE",
    "Total Memory Usage Error Threshold": "90",
    "Total Memory Usage Warning Alarm": "FALSE",
    "Total Memory Usage Warning Threshold": "50",
    "Physical Memory Usage Error Alarm": "FALSE",
    "Physical Memory Usage Error Threshold": "95",
    "Physical Memory Usage Warning Alarm": "FALSE",
    "Physical Memory Usage Warning Threshold": "85",
    "Swap Memory Usage Error Alarm": "FALSE",
    "Swap Memory Usage Error Threshold": "85",
    "Swap Memory Usage Warning Alarm": "FALSE",
    "Swap Memory Usage Warning Threshold": "60",
    "Paging Error Alarm Active": "FALSE",
    "Paging Error Alarm Threshold": "400",
    "Paging Warning Alarm Active": "FALSE",
    "Paging Warning Alarm Threshold": "150"
}

# The agent's name we wish to configure.
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

# Creating an SoftLayer_Monitoring_Agent_Configuration_Value skeleton
# which contains the configuration for the agent.
configurationValues = []
for item in configuration.keys():
    itemFound = False
    for value in agent['configurationValues']:
        if value['definition']['name'].strip().upper() == item.strip().upper():
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
    result = monitoringService.applyConfigurationValues(configurationValues, id=agent['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to apply the configuration in the monitoring agent: faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
