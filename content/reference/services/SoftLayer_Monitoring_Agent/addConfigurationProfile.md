---
title: "addConfigurationProfile"
description: "This method is used to apply changes to a monitoring agent's configuration for SoftLayer_Configuration_Template_Section... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/addConfigurationProfile"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::addConfigurationProfile

Creates a transaction that for adding additional monitoring configuration.


## Overview 
This method is used to apply changes to a monitoring agent's configuration for SoftLayer_Configuration_Template_Section with the property sectionType that has a keyName of 'TEMPLATE_SECTION'. Configuration values that are passed in can be new or updated objects but must have a definitionId and profileId defined for both. Existing SoftLayer_Monitoring_Agent_Configuration_Value values can be retrieved as a property of the SoftLayer_Configuration_Template_Section_Definition's from the monitoring agent's configurationTemplate property. New values will follow the structure of SoftLayer_Monitoring_Agent_Configuration_Value. It returns a SoftLayer_Provisioning_Version1_Transaction object to track the progress of the update being applied. Some configuration sections act as a template which helps to create additional monitoring configurations. For instance, Core Resource monitoring agent lets you create monitoring configurations for different disk volumes or disk path. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationValues| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>| Array of values to be set for the|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>


### associatedMethods

*  [SoftLayer_Monitoring_Agent::deleteConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )

