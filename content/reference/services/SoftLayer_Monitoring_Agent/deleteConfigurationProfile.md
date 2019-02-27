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
aliases:
    - "/reference/services/softlayer_monitoring_agent/deleteConfigurationProfile"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::deleteConfigurationProfile

This method deletes a configuration profile from a monitoring agent.


## Overview 
This method will remove a SoftLayer_Configuration_Template_Section_Profile from a SoftLayer_Configuration_Template_Section by passing in the sectionId of the profile object and identifier of the profile. This will execute the action immediately on the server and the SoftLayer_Configuration_Template_Section returning a boolean true if successful. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|sectionId| integer| SoftLayer_Configuration_Template_Section identifier|
|profileId| integer| SoftLayer_Configuration_Template_Section_Profile identifier|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )



### Error Handling

* SoftLayer_Exception 

> Throws 'Your monitoring agent "{monitoringAgentName}" is inactive.' if the monitoring agent's status code is not 'ACTIVE'. 

* SoftLayer_Exception 

> Throws 'Failed to find a remote monitoring resource.' if the remote monitoring identifier is not found. 

* SoftLayer_Exception 

> Throws 'Monitoring agent cannot be found on a remote resource. Please contact development .' if the configuration deleted by the agent is not found. 

* SoftLayer_Exception 

> Throws 'Failed to delete configuration profile "{profileName}".' if an exception is caught while attempted to delete the configuration section. 

* SoftLayer_Exception 

> Throws 'No profile was found.' if no profile was found. 

* SoftLayer_Exception_Public 

> Throws 'You cannot delete a profile in "{sectionName}" configuration section.' if the section has the disallowedDeletionFlag property set to true. 



