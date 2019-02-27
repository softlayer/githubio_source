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

-----

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
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>


### Associated Methods

*  [SoftLayer_Monitoring_Agent::deleteConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )



### Error Handling

* SoftLayer_Exception 

> Throws 'You must provide an array of modified configuration value objects.' if the configurationValues parameter is not an array. 

* SoftLayer_Exception 

> Throws 'Your monitoring agent "{monitoringAgentName}" is inactive.' if the monitoring agent's status code is not 'ACTIVE'. 

* SoftLayer_Exception 

> Throws 'Configuration definition id must be provided when adding a new value.' if a configuration definition identifier is not set on one of the values. 

* SoftLayer_Exception 

> Throws 'Invalid configuration definition id of {configurationDefinitionId}' if a value's configuration definition identifier is invalid. 

* SoftLayer_Exception 

> Throws 'Duplicate configuration value for definition "{definitionName}".' if a value for a definition is included more than once in the configuration values array. 

* SoftLayer_Exception 

> Throws '{definitionName} cannot be empty.' if the SoftLayer_Monitoring_Agent_Configuration_Value's value is empty. 

* SoftLayer_Exception 

> Throws 'Configuration definition Id {definitionIdentifier}"{definitioName}" does not belong to this monitoring agent.' if the monitoring agent's configuration template identifier does not match the definition's section template identifier or if the monitoring agent's configuration template's parent identifier does not match the definition's section template identifier. 

* SoftLayer_Exception 

> Throws 'You can only add a single configuration section at a time.' if the definition's section identifier does not match the definitions section identifier nor the definition's section parent identifier. 

* SoftLayer_Exception 

> Throws 'You have reached the maximum monitoring object count of {countRestrictionValue} for "{sectionName}".' if the configuration profiles count equals or exceeds the count restriction's value. 

* SoftLayer_Exception 

> Throws 'Configuration definition "{definitionToCheckName}" is required.' if any of the section definition's require value flag is set to true and is not included in the configuration values, or if a definition section has sub-sections and any of those sub-sections have a require value flag set to true and is not included in the configuration values. 

* SoftLayer_Exception 

> Throws 'Configuration profile name is required.' if a SoftLayer_Monitoring_Agent_Configuration_Value is null. 

* SoftLayer_Exception 

> Throws 'You already have configured to monitor "{profileValue}" for "{profileValueDefinitionName}".' if a SoftLayer_Monitoring_Agent_Configuration_Value already exists for this SoftLayer_Monitoring_Agent. 

* SoftLayer_Exception 

> Throws 'No change has been made.' if no transactions are being created to change the configuration profile. 

* SoftLayer_Exception 

> Throws a new-line separated list of error messages if any of the SoftLayer_Monitoring_Agent_Configuration_Value values are invalid or incomplete. 

* SoftLayer_Exception_Public 

> Throws '"{definitionName}" requires a value that is smaller than 100 characters in length.' if a SoftLayer_Monitoring_Agent_Configuration_Value value is greater or equal to 100 characters in length. 

* SoftLayer_Exception_Public 

> Throws '"{definitionName}" value has an invalid character: |' if a SoftLayer_Monitoring_Agent_Configuration_Value value contains a '|' character. 



