---
title: "deleteConfigurationProfile"
description: "This method will remove a SoftLayer_Configuration_Template_Section_Profile from a SoftLayer_Configuration_Template_Secti... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::deleteConfigurationProfile

This method deletes a configuration profile from a monitoring agent.


## Overview 
This method will remove a SoftLayer_Configuration_Template_Section_Profile from a SoftLayer_Configuration_Template_Section by passing in the sectionId of the profile object and identifier of the profile. This will execute the action immediately on the server and the SoftLayer_Configuration_Template_Section returning a boolean true if successful. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|sectionId| integer| SoftLayer_Configuration_Template_Section identifier|
|profileId| integer| SoftLayer_Configuration_Template_Section_Profile identifier|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )

