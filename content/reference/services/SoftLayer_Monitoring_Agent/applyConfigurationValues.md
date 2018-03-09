---
title: "applyConfigurationValues"
description: "This method creates a transaction used to apply changes to a monitoring agent's configuration for an array of SoftLayer_... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::applyConfigurationValues

Creates a transaction that applies monitoring configuration value changes to a monitoring agent's configuration for fixed sections. 


## Overview 
This method creates a transaction used to apply changes to a monitoring agent's configuration for an array of SoftLayer_Configuration_Template_Section that have the property sectionType with a name of 'Fixed section'. Configuration values that are passed in can be new or updated objects but must have a configurationDefinitionId defined for both. Existing SoftLayer_Monitoring_Agent_Configuration_Value values can be retrieved as a property of the SoftLayer_Configuration_Template_Section_Definition from the monitoring agent's configurationTemplate property. New values will follow the structure of SoftLayer_Monitoring_Agent_Configuration_Value. This method returns a SoftLayer_Provisioning_Version1_Transaction object to track the progress of the update being applied. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationValues| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>| Array of value objects to be applied|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>


### associatedMethods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::deleteConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::deployMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent )
*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationTemplates](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationTemplates )
*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues )
*  [SoftLayer_Monitoring_Agent::getGraph](/reference/services/SoftLayer_Monitoring_Agent/getGraph )

