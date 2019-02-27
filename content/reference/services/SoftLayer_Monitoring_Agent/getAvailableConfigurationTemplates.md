---
title: "getAvailableConfigurationTemplates"
description: "This method returns an array of available SoftLayer_Configuration_Template objects for this monitoring agent."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/getAvailableConfigurationTemplates"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getAvailableConfigurationTemplates

Returns available configuration templates for this monitoring agent.


## Overview 
This method returns an array of available SoftLayer_Configuration_Template objects for this monitoring agent. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template[] </a>


### Associated Methods

*  [SoftLayer_Monitoring_Agent::deployMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent )



### Error Handling

* SoftLayer_Exception 

> Throws 'You do not have access to this monitoring agent.' if the active user is an instance of SoftLayer_User_Customer and the account identifier associated with this SoftLayer_Monitoring_Agent's robot is not the same as the account identifier for the active user. 



