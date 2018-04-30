---
title: "clone_configuration_template.py"
description: "clone_configuration_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Configuration_Template"
tags:
    - "monitoring"
---


```
"""
Create a monitoring configuration template and a template group

The script clones an existent configuration template performs a change in the
configuration template then creates a template group and adds the created
configuration template to the new template group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Configuration_Template
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
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
        {
            "configurationTemplateId": newTemplateId
        },
        {
            "configurationTemplateId": processMonitoringAgent
        },
        {
            "configurationTemplateId": windowsServiceMonitoringAgent
        },
        {
            "configurationTemplateId": remoteMonitoringAgent
        }
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
