---
title: "view_agent_report_disk_profile.py"
description: "view_agent_report_disk_profile.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Metric_Data_Type"
    - "SoftLayer_Hardware_Server"
tags:
    - "monitoring"
---


```
"""
View the reports for the  "Disk Profile" section from the
'Cpu, Disk, and Memory Monitoring Agent' monitor agent.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData
http://sldn.softlayer.com/reference/services/Monitoring_Agent_Configuration_Value/getMetricDataType

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# The IP address of the server or VSI to configure.
ipAddres = "5.153.59.197"

startDate = '2016-01-02'
endDate = '2016-01-08'

# Set "True" the reports you wish to see.
reports = {
    'Graph Disk Usage': "TRUE",
    'Graph Disk Usage as Percentage': "False"
}

# The profile you wish to see the reports.
profile = 'p:\\'

# The agent's name we wish to see the reports.
agentName = 'Cpu, Disk, and Memory Monitoring Agent'

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']
hardwareService = client['SoftLayer_Hardware_Server']
monitoringService = client['SoftLayer_Monitoring_Agent']
agentConfigurationService = client['Monitoring_Agent_Configuration_Value']

# Getting the monitoring agents installed in the server or VSI.
try:
    # Setting an object mask to retrieve information about the monitoring agents.
    objectMask = 'mask[monitoringAgents[configurationValues[definition]]]'
    server = vsiService.findByIpAddress(ipAddres, mask=objectMask)
    if not 'id' in server:
        server = hardwareService.findByIpAddress(ipAddres, mask=objectMask)
        if not 'id' in server:
            print("There is no a Server or VSI with the IP address: " + ipAddres)
            exit(1)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to activate the monitor agent: faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

# Getting the agent to see the reports.
agents = [agent for agent in server['monitoringAgents'] if agent['name'] == agentName]
if len(agents) == 0:
    print("Unable to find the agent: " + agentName)
    exit(1)
agent = agents[0]

# Getting the profile id to edit.
profileId = [value['profileId'] for value in agent['configurationValues'] if
             value['definition']['name'] == 'Disk Path' and
             value['value'].strip().upper() == profile.strip().upper()]
if len(profileId) == 0:
    print("The profile " + profile + " was mot found")
    exit(1)
profileId = profileId[0]

# Creating the list of SoftLayer_Container_Metric_Data_Type objects
metricDataTypes = []
for item in reports.keys():
    if reports[item].strip().upper() == "TRUE":
        itemFound = False
        for value in agent['configurationValues']:
            if value['definition']['name'].strip().upper() == item.strip().upper() and value['profileId'] == profileId:
                itemFound = True
                if value['value'].strip().upper() == "TRUE":
                    try:
                        metrics = agentConfigurationService.getMetricDataType(id=value['id'])
                        metricDataTypes.append(metrics)
                    except SoftLayer.SoftLayerAPIError as e:
                        print("Unable to get the metrics. " % (e.faultCode, e.faultString))
                else:
                    print("The report: " + item + " is disable for the agent. Please review the agent configuration.")
                    exit(1)
                break
        if not itemFound:
            print("The configuration: " + item + " is not available for the agent.")

# Getting the reports.
try:
    data = monitoringService.getGraphData(metricDataTypes, startDate, endDate, id=agent['id'])
    print(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to activate the monitor agent: faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))

```
