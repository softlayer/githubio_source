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
---
# SoftLayer_Monitoring_Agent::getAvailableConfigurationValues
## Overview 
Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent is running on. For example, invoking this method against "Network Traffic Monitoring Agent" will return all available network adapters on your system. 

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
<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>
