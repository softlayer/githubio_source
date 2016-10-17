---
title: "Monitoring Examples"
description: "A few examples on how to interact with SoftLayer Monitoring"
date: "2016-10-12"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Monitoring_Agent"
tags:
    - "monitoring"
---


ResponseStatus codes and what they mean.
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Result

* 0: CRITICAL 
* 1: Warning 
* 2: OK  
* 4 - 5: Unknown Status, Contact Support

More information:
https://stackoverflow.com/questions/37662607/python-api-monitoring-manager

This example gets the status of your Basic and Advanced monitoring.
```python

import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):
        return True

    def getBasicStatus(self, server_id):
        mask = "mask[fullyQualifiedDomainName, networkMonitors[lastResult]]"
        server = self.client['SoftLayer_Virtual_Guest'].getObject(id=server_id, mask=mask )
        pp(server)

    def getAdvancedStatus(self, server_id):
        mask = "mask[fullyQualifiedDomainName, monitoringAgents[configurationValues[definition]]]"
        server = self.client['SoftLayer_Virtual_Guest'].getObject(id=server_id, mask=mask )
        pp(server)

if __name__ == "__main__":
    server = 24880113
    main = example()
    main.getBasicStatus(server)
    main.getAdvancedStatus(server)
```



This example configures the CPU monitor
```
"""
Configure the section 'CPU' from the 'Cpu, Disk, and Memory Monitoring Agent' agent.

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
ipAddres = "159.8.52.188"

configuration = {
    'Graph System CPU Usage': "False",
    'Graph Total CPU Usage': "False",
    'Graph User CPU Usage': "True",
    'Graph I/O Wait CPU Usage': "True",
    'Processor Queue Length Alarm': "True",
    'CPU Usage Error Alarm': "True",
    'CPU Usage Error Alarm Threshold': "99",
    'CPU Usage Warning Alarm': "True",
    'CPU Usage Warning Alarm Threshold': "82",
    'Processor Queue Length Alarm': "True",
    'Max Queue Length': "4"
}

# The agent's name we wish to configure.
agentName = 'Cpu, Disk, and Memory Monitoring Agent'

client = SoftLayer.Client()
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
    print("Unable to get the server "
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
    print("Unable to apply the configuration in the monitoring agent."
          % (e.faultCode, e.faultString))
    exit(1)
```



This example GETs the monitoring configuration

```python
"""
Get the configuration of the monitoring agent in a server or VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent/
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

ipAddres = "169.54.54.164"

client = SoftLayer.Client()
vsiService = client['SoftLayer_Virtual_Guest']
hardwareService = client['SoftLayer_Hardware_Server']

try:
    objectMask = 'mask[monitoringAgents[configurationTemplate[configurationSections[subSections]],' \
                 'configurationValues[id, value, profileId, agentId, configurationDefinitionId,' \
                 'profile, definition[attributes, section, valueType]]]]'
    server = vsiService.findByIpAddress(ipAddres, mask=objectMask)
    if not 'id' in server:
        server = hardwareService.findByIpAddress(ipAddres, mask=objectMask)
        if not 'id' in server:
            print("There is no a Server or VSI with the IP address: " + ipAddres)
            exit(1)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the server "
          % (e.faultCode, e.faultString))
    exit(1)

# We will get the configuration of the active agents
agents = [agent for agent in server['monitoringAgents'] if agent['statusName'] == "Active"]
server['monitoringAgents'] = agents

configs = []
for agent in server['monitoringAgents']:
    config = {}
    config['agent'] = agent['name']
    config['id'] = agent['id']
    sections = []
    for section in agent['configurationTemplate']['configurationSections']:
        sect = {}
        subsects = []
        hasProfile = False
        profileIds = []
        confs = []
        for subsection in section['subSections']:
            values = [value for value in agent['configurationValues'] if
                      value['definition']['sectionId'] == subsection['id']]
            for value in values:
                conf = {}
                if value['profileId'] == "":
                    conf[value['definition']['name']] = value['value']
                    confs.append(conf)
                else:
                    hasProfile = True
                    profileIds.append(value['profileId'])      
        sect['name'] = section['name']
        if not hasProfile:
            sect['configuration'] = confs
            sections.append(sect)
        else:
            profileIds = list(set(profileIds))
            profiles = []
            for profileId in profileIds:
                profile = {}
                valueConfs = []
                valueProfiles = [value for value in agent['configurationValues'] if
                                 value['profileId'] == profileId]
                profile['name'] = valueProfiles[0]['profile']['name']
                for valueProfile in valueProfiles:
                    value = {}
                    value[valueProfile['definition']['name']] = valueProfile['value']
                    valueConfs.append(value)
                profile['configuration'] = valueConfs
                profiles.append(profile)
            sect['profiles'] = profiles
            sections.append(sect)
    config['sections'] = sections
    configs.append(config)
print(json.dumps(configs, sort_keys=True, indent=2, separators=(',', ': ')))
```


This example views the results of the monitoring

```python
"""
View the reports for the  "CPU" section from the
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
ipAddres = "159.8.52.188"

startDate = '2016-01-02'
endDate = '2016-01-08'

# Set "True" the reports you wish to see.
reports = {
    'Graph System CPU Usage': "False",
    'Graph Total CPU Usage': "False",
    'Graph User CPU Usage': "False",
    'Graph I/O Wait CPU Usage': "True",
}

# The agent's name we wish to see the reports.
agentName = 'Cpu, Disk, and Memory Monitoring Agent'

client = SoftLayer.Client()
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
    print("Unable to get the server "
          % (e.faultCode, e.faultString))
    exit(1)

# Getting the agent to see the reports.
agents = [agent for agent in server['monitoringAgents'] if agent['name'] == agentName]
if len(agents) == 0:
    print("Unable to find the agent: " + agentName)
    exit(1)
agent = agents[0]

# Creating the list of SoftLayer_Container_Metric_Data_Type objects
metricDataTypes = []
for item in reports.keys():
    if reports[item].strip().upper() == "TRUE":
        itemFound = False
        for value in agent['configurationValues']:
            if value['definition']['name'].strip().upper() == item.strip().upper():
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
    print("Unable to get the report. "  % (e.faultCode, e.faultString))
```