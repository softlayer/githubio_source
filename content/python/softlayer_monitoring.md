---
title: "Monitoring Agent Management"
description: "A collection of examples on how to interact with the Monitoring Agent"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
    - "SoftLayer_Configuration_Template"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_User_Customer"
    - "SoftLayer_Monitoring_Agent_Configuration_Value"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Metric_Data_Type"
tags:
    - "monitoring"
---


ResponseStatus codes and what they mean.
+ http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Result

* 0: CRITICAL 
* 1: Warning 
* 2: OK  
* 4 - 5: Unknown Status, Contact Support


### Ordering Monitoring
Build a SoftLayer_Container_Product_Order_Monitoring_Package object for a new
monitoring order and pass it to the SoftLayer_Product_Order API service to order it
In this care we'll order a Basic (Hardware and OS) package with Basic Monitoring Package - Linux configuration.

Important manual pages:

+ https://softlayer.github.io/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
+ http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
+ http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group

```python
"""
Order a Monitoring Package
"""
import SoftLayer

"""
Build a skeleton SoftLayer_Container_Product_Order_Monitoring_Package object
containing the order you wish to place.
"""
oderTemplate = {
    'complexType': 'SoftLayer_Container_Product_Order_Monitoring_Package',
    'packageId': 0,  # the packageID for order monitoring packages is 0
    'prices': [
        {'id': 2302}  # this is the price for Monitoring Package - Basic ((Hardware and OS))
    ],
    'quantity': 0,  # the quantity for order a service (in this case monitoring package) must be 0
    'sendQuoteEmailFlag': True,
    'useHourlyPricing': True,
    'virtualGuests': [
        {'id': 4906034}  # the virtual guest ID where you want add the monitoring package
    ],
    'configurationTemplateGroups': [
        {'id': 3}  # the templateID for the monitoring group (in this case Basic Monitoring package for Unix/Linux operating system.)
    ]
}

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client()
productOrderService = client['SoftLayer_Product_Order']

"""
verifyOrder() will check your order for errors. Replace this with a call to
placeOrder() when you're ready to order. Both calls return a receipt object
that you can use for your records.

Once your order is placed it'll go through SoftLayer's provisioning process.
"""

order = productOrderService.verifyOrder(oderTemplate)
print(order)

```


### Activate Monitoring Agent

Important manual pages:

+ https://softlayer.github.io/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ https://softlayer.github.io/reference/services/SoftLayer_Monitoring_Agent/activate

```python
"""
Active an agent.
"""

import SoftLayer
import json

vsiIp = "169.45.98.148"
agentName = "DHCP Response Monitoring Agent"


client = SoftLayer.Client()
vsiService = client['SoftLayer_Virtual_Guest']
agentService = client['SoftLayer_Monitoring_Agent']


objectMask = "mask[monitoringRobot[id, robotStatus[name]], monitoringAgents[statusName, name, id], monitoringServiceEligibilityFlag, datacenter]"
vsi = vsiService.findByIpAddress(vsiIp, mask=objectMask)
if not vsi:
    print("There is not a vsi with the IP address: " + vsiIp)
    exit(1)
agent = {}
for agents in vsi['monitoringAgents']:
    if agents['name'].strip().upper() == agentName.strip().upper():
        agent = agents
        break
if not 'id' in agent:
    print("The VSI does not have a monitor agent with the name: " +  agentName)
    exit(1)
result = agentService.activate(id=agent['id'])
print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

```

### Add/Remove Monitoring Subscriber
The scripts adds subscribers to an arbitrary VSI machine.

Important manual pages:

+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringAgents
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber

```python
"""
Add subscribers to a monitor
"""
import SoftLayer

hostnames = ["rctest", "rctest2"]
mailsToAdd = ["someone@test.com", "someone.else@test.com"]

client = SoftLayer.Client()
# Getting all virtual servers on the account
vServers = client['Account'].getVirtualGuests()
for hostname in hostnames:
    for vServer in vServers:
        if hostname == vServer['hostname']:
            vSertverId = vServer['id']
            # Getting all the agents in the virtual machine
            agents = client['Virtual_Guest'].getMonitoringAgents(id=vSertverId)
            for agent in agents:
                agentId = agent['id']
                agentName = agent['name']
                elegibleSubscribers = client['SoftLayer_Monitoring_Agent'].getEligibleAlarmSubscibers(id=agentId)
                for mailToAdd in mailsToAdd:
                    for elegibleSubscriber in elegibleSubscribers:
                        if 'id' in elegibleSubscriber:
                            suscriberId = elegibleSubscriber['id']
                            userData = client['SoftLayer_User_Customer'].getObject(id=suscriberId)
                            if mailToAdd.strip() == userData['email'].strip():
                                added = client['SoftLayer_Monitoring_Agent'].setActiveAlarmSubscriber(suscriberId, id=agentId)
                                # Use this to Remove 
                                # removed = client['SoftLayer_Monitoring_Agent'].removeActiveAlarmSubscriber(suscriberId, id=agentId)
                                if added:
                                    print("For hostname: " + hostname + " with ID " + str(vSertverId) + " in the agent for " + agentName + " the mail " + mailToAdd + " has been added.")
                                else:
                                    print("ERROR - For hostname: " + hostname + " with ID " + str(vSertverId) + " in the agent for " + agentName + " the mail " + mailToAdd + " has not been added.")



```

### Clone monitoring configuration
The script clones an existing configuration template, performs a change in the
configuration template, then creates a template group and adds the created
configuration template to the new template group.

Important manual pages:

+ https://softlayer.github.io/reference/services/SoftLayer_Configuration_Template
+ https://softlayer.github.io/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group
+ https://softlayer.github.io/reference/services/SoftLayer_Product_Package

```python
"""
Create a monitoring configuration template and a template group

"""
import SoftLayer


client = SoftLayer.Client()
configurationTemplateService = client['SoftLayer_Configuration_Template']
monitoringAgentConfigurationTemplateGroupService = client['SoftLayer_Monitoring_Agent_Configuration_Template_Group']
productPackageService = client['SoftLayer_Product_Package']

templates = configurationTemplateService.getAllObjects(limit=100, offset=0)
newTemplateId = -1
for template in templates:
    if template['name'] == 'CDM Monitoring agent-MH-Linux v2':
        # Creating an Skeleton SoftLayer_Configuration_Template for our new template
        templateObject = {
            'description': 'this is my clone test',
            'name': 'clone for test',
            'parentId': template['id']
        }
        newTemplate = configurationTemplateService.copyTemplate(templateObject, id=template['id'])
        # Getting the definitions from the parent template to set in the new template e.g. CPU, Memory
        objectMask = 'mask[configurationSections[subSections[definitions]]]'
        definitions = configurationTemplateService.getObject(mask=objectMask, id=template['id'])

        # The configuration values for our new template
        configurationValues = []

        """
        We are going to define the configuration for our template by default it has the
        same configuration as the parent template.
        we are looking a determinate configuration section in this case CPU section.
        """
        for definition in definitions['configurationSections']:
            if definition['name'] == 'CPU':
                # We are looking for the subsection Graphing.
                for subsection in definition['subSections']:
                    if subsection['name'] == 'Graphing':
                        for subdefinition in subsection['definitions']:
                            # We are looking the 'Graph Total CPU Usage' configuration option.
                            if subdefinition['name'] == 'Graph Total CPU Usage':
                                # Setting the configuration for our template
                                configurationValues.append({"definitionId": subdefinition['id'], "templateId": template['id'], "value": "FALSE"})

        print(configurationValues)
        # Updating the new configuration in our created template
        result = configurationTemplateService.updateDefaultValues(configurationValues, id=newTemplate['id'])
        newTemplateId = newTemplate['id']
        print(result)


"""
Looking for a monitoring package in order to add our new template group
in that monitoring package. In this case we are going to add it to
"Monitoring Package - Basic"
"""
monitoringBasicId = -1
itemsPackage = productPackageService.getItems(id=0)
for item in itemsPackage:
    if item['description'] == "Monitoring Package - Basic":
        monitoringBasicId = item['id']
        break

"""
To create a template group in "Monitoring package - Basic"
is necessary to specific a configuration template for
Cpu, Disk, and Memory Monitoring Agent
Process Monitoring Agent
Windows Services Monitoring Agent
Remote System Monitoring Agent
we are going to look for the IDs for those configuration templates
except for "Cpu, Disk, and Memory Monitoring Agent", for this we are going
to use the template that we created above
"""
templates = configurationTemplateService.getAllObjects(limit=100, offset=0)
cpuDiskMemoryMonitoringAgent = newTemplateId
processMonitoringAgent = -1
windowsServiceMonitoringAgent = -1
remoteMonitoringAgent = -1
for template in templates:
    if template['name'] == "Process Monitoring Agent ":
        proccesMonitoringAgent = template['id']
    if template['name'] == "Windows Services Monitoring Agent":
        windowsServiceMonitoringAgent = template['id']
    if template['name'] == "Remote system monitoring agent - Linux V1":
        remoteMonitoringAgent = template['id']

"""
Creating an skeleton SoftLayer_Monitoring_Agent_Configuration_Template_Group for our
new template group
"""
templateObject = {
    "description": "this is my template group test",
    "itemId": monitoringBasicId,
    "name": "my template group test",
    "configurationTemplateReferences": [
        {"configurationTemplateId": newTemplateId},
        {"configurationTemplateId": processMonitoringAgent},
        {"configurationTemplateId": windowsServiceMonitoringAgent},
        {"configurationTemplateId": remoteMonitoringAgent}
    ]
}

try:
    result = monitoringAgentConfigurationTemplateGroupService.createObject(templateObject)
    print(result)

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the object template for the monitoring agent. "
          % (e.faultCode, e.faultString))
    exit(1)

```


### Configure Monitoring Agent

Important manual pages
+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues
+ http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value

```python
"""
Configure the section 'CPU' from the 'Cpu, Disk, and Memory Monitoring Agent' agent.

"""

import SoftLayer
import json

# The IP address of the server or VSI to configure.
ipAddres = "23.246.195.66"

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

### Configure new agent disk profile

Important manual pages
+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile
+ http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value

```python
"""
Create a new 'Disk Profile' configuration for the 'Cpu, Disk, and Memory Monitoring Agent' agent.

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

client = SoftLayer.Client()
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

### Configure Agent Memory Profile
Important manual pages
+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues
+ http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value

```python
"""
Configure the section 'Memory' from the 'Cpu, Disk, and Memory Monitoring Agent' agent.

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

### Edit Agent Profile
Important manual pages

+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile
+ http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value

```python
"""
Edit the configuration for the "Disk Profile" section
of a monitoring agent.

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

### Deactive Agent
Important manual pages:

+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/deactivate

```python
"""
Desactive an agent.
"""

import SoftLayer
import json

vsiIp = "169.45.98.148"
agentName = "DHCP Response Monitoring Agent"

client = SoftLayer.Client(
vsiService = client['SoftLayer_Virtual_Guest']
agentService = client['SoftLayer_Monitoring_Agent']


objectMask = """mask[monitoringRobot[id, robotStatus[name]], monitoringAgents[statusName, name, id], monitoringServiceEligibilityFlag, datacenter]"""
vsi = vsiService.findByIpAddress(vsiIp, mask=objectMask)
if not vsi:
    print("There is no a vsi with the IP address: " + vsiIp)
    exiΩt(1)
agent = {}
for agents in vsi['monitoringAgents']:
    if agents['name'].strip().upper() == agentName.strip().upper():
        agent = agents
        break
if not 'id' in agent:
    print("The VSI does not have a monitor agent with the name: " +  agentName)
    exit(1)
result = agentService.deactivate(id=agent['id'])
print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

```

### Get Agent Configuration
```python
"""
Get the configuration of the monitoring agent in a server or VSI.
"""

import SoftLayer
import json

ipAddres = "5.153.59.197"
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
    print("Unable to get the server: faultCode=%s, faultString=%s"        
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

### Get monitoring graph data
The script gets the CPU usage in a selected date range. 

Important manual pages.
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData

```python
"""
Get the graph data from a monitoring agent
"""
import SoftLayer

# This data can take a little while to obtain for long date ranges
TIMEOUT = 12000

"""
Creating an skeleton SoftLayer_Container_Metric_Data_Type object
which represent the metric data that we will get.
"""
metricDataTypes = [
    {
        "summaryType": "average",
        "keyName": "CDM_CPU_USAGE",
        "name": "cdm_cpu_usage_U3lzdGVt"
    }
]

# The start date for the graph data
starDate = "2014-09-29T01:48:08.474Z"
# The end date for the graph data
endDate = "2014-09-29T01:53:08.474Z"
"""
The agent ID from where we want to get the graph data
to get the monitor agents in your virtual guest
call the SoftLayer_Virtual_Guest::getMonitoringAgents method
"""
agentId = 1448912

client = SoftLayer.Client(timeout=TIMEOUT)
monitorAgentService = client['SoftLayer_Monitoring_Agent']
# calling the Softlayer_Monitoring_Agent::getGraphData method
result = monitorAgentService.getGraphData(
    metricDataTypes, starDate, endDate, id=agentId)
print(result)
```
### View Agent Report
Important manual pages
+ http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
+ http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData
+ http://sldn.softlayer.com/reference/services/Monitoring_Agent_Configuration_Value/getMetricDataType

```python
"""
View the reports for the  "CPU" section from the
'Cpu, Disk, and Memory Monitoring Agent' monitor agent.
"""
import SoftLayer
import json

# The IP address of the server or VSI to configure.
ipAddres = "5.153.59.197"

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

# Setting an object mask to retrieve information about the monitoring agents.
objectMask = 'mask[monitoringAgents[configurationValues[definition]]]'
server = vsiService.findByIpAddress(ipAddres, mask=objectMask)
if not 'id' in server:
    server = hardwareService.findByIpAddress(ipAddres, mask=objectMask)
    if not 'id' in server:
        print("There is no a Server or VSI with the IP address: " + ipAddres)
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
data = monitoringService.getGraphData(metricDataTypes, startDate, endDate, id=agent['id'])
print(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
```

### Create Ping Monitor
The script creates a Network Notification of type  service ping
and a notify wait of 5 minutes.

```python
"""
Create Network Notification
"""
import SoftLayer
# Declare the API client
client = SoftLayer.Client()
networkMonitorService = client['SoftLayer_Network_Monitor_Version1_Query_Host']

objectTemplate = [
    {
        "guestId": 6143038,
        "ipAddress": "10.104.50.118",
        "queryTypeId": 1,
        "responseActionId": 2,
        "waitCycles": 1
    }
]
result = networkMonitorService.createObjects(objectTemplate)
print(result)
```

### Redeploy or Restart Agent

```python
"""
Re-deploy an agent.
"""

import SoftLayer
import json

vsiIp = "169.45.98.148"
agentName = "DHCP Response Monitoring Agent"
client = SoftLayer.Client()
vsiService = client['SoftLayer_Virtual_Guest']
agentService = client['SoftLayer_Monitoring_Agent']


objectMask = "mask[monitoringRobot[id, robotStatus[name]], monitoringAgents[statusName, name, id], monitoringServiceEligibilityFlag, datacenter]"
vsi = vsiService.findByIpAddress(vsiIp, mask=objectMask)
if not vsi:
    print("There is no a vsi with the IP address: " + vsiIp)
    exit(1)
agent = {}
for agents in vsi['monitoringAgents']:
    if agents['name'].strip().upper() == agentName.strip().upper():
        agent = agents
        break
if not 'id' in agent:
    print("The VSI does not have a monitor agent with the name: " +  agentName)
    exit(1)
configuration = agentService.getConfigurationTemplate(id=agent['id'])
result = agentService.deployMonitoringAgent(configuration['id'], id=agent['id'])
# Restarts the Agent instead
# result = agentService.restartMonitoringAgent(id=agent['id'])
print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
```


