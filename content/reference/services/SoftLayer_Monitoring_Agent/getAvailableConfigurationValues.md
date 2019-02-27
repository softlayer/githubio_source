---
title: "getAvailableConfigurationValues"
description: "Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/getAvailableConfigurationValues"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getAvailableConfigurationValues

Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent is running on. 


## Overview 
Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent is running on. For example, invoking this method against "Network Traffic Monitoring Agent" will return all available network adapters on your system. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationDefinitionId| integer| $configurationDefinitionId Numeric configuration|
|configValues| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>| Optional array of|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>


### Associated Methods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )
*  [SoftLayer_Monitoring_Agent::getGraph](/reference/services/SoftLayer_Monitoring_Agent/getGraph )



### Error Handling

* SoftLayer_Exception 

> Throws 'Monitoring agent is not active.' if this SoftLayer_Monitoring_Agent's status code is not 'ACTIVE'. 

* SoftLayer_Exception 

> Throws 'Invalid configuration definition id is provided.' if the configuration definition identifier is not numeric. 

* SoftLayer_Exception 

> Throws 'Configuration definition id does not belong to this monitoring agent.' if there is no SoftLayer_Configuration_Template_Section_Definition id for the specified configurationDefinitionId. 

* SoftLayer_Exception 

> Throws '"{definitionName}" does not have available configuration values.' if the SoftLayer_Configuration_Template_Section_Definition for the specified configurationDefinitionId does not have a valueType keyname of 'RESOURCE_SPECIFIC_DATA'. 

* SoftLayer_Exception 

> Throws 'Configuration definition requires more information to retrieve section-specific values.' if the SoftLayer_Configuration_Template_Section_Definition for the specified configurationDefinitionId has the attribute 'MONITORING_SECTION_SPECIFIC_PROFILE', but it's section template configurationSections does not include a SoftLayer_Configuration_Template_Section_Definition attribute of 'MONITORING_SECTION_SPECIFIC_PROFILE'. 

* SoftLayer_Exception 

> Throws 'Configuration definition requires more information to retrieve resource-specific values.' if the SoftLayer_Configuration_Template_Section_Definition for the specified configurationDefinitionId does not have the attribute 'MONITORING_SECTION_SPECIFIC_PROFILE' and does not have either 'MONITORING_RESOURCE_SPECIFIC_VALUE_METHOD' or 'MONITORING_RESOURCE_SPECIFIC_VALUE_PATH' attributes. 



