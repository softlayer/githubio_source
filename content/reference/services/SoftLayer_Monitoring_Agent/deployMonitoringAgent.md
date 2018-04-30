---
title: "deployMonitoringAgent"
description: "Initialize a monitoring agent and deploy it with the SoftLayer_Configuration_Template with the same identifier as the $c... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/deployMonitoringAgent"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::deployMonitoringAgent

Initialize a monitoring agent and deploy it with the specified configuration template. 


## Overview 
Initialize a monitoring agent and deploy it with the SoftLayer_Configuration_Template with the same identifier as the $configurationTemplateId parameter. If the configuration template ID is not provided, the current configuration template will be used. When executing this method, the existing configuration values will be lost. If no configuration template identifier is provided, the current configuration template will be used. '''Warning''' Reporting data may be lost as a result of executing this method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationTemplateId| integer| The numeric identifier for the SoftLayer_Configuration_Template to use when|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>


### associatedMethods

*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationTemplates](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationTemplates )
*  [SoftLayer_Monitoring_Agent::activate](/reference/services/SoftLayer_Monitoring_Agent/activate )
*  [SoftLayer_Monitoring_Agent::deactivate](/reference/services/SoftLayer_Monitoring_Agent/deactivate )

