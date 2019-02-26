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
aliases:
    - "/reference/services/softlayer_monitoring_agent/applyConfigurationValues"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::applyConfigurationValues

Creates a transaction that applies monitoring configuration value changes to a monitoring agent's configuration for fixed sections. 


## Overview 
This method creates a transaction used to apply changes to a monitoring agent's configuration for an array of SoftLayer_Configuration_Template_Section that have the property sectionType with a name of 'Fixed section'. Configuration values that are passed in can be new or updated objects but must have a configurationDefinitionId defined for both. Existing SoftLayer_Monitoring_Agent_Configuration_Value values can be retrieved as a property of the SoftLayer_Configuration_Template_Section_Definition from the monitoring agent's configurationTemplate property. New values will follow the structure of SoftLayer_Monitoring_Agent_Configuration_Value. This method returns a SoftLayer_Provisioning_Version1_Transaction object to track the progress of the update being applied. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>


### Associated Methods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::deleteConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::deployMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent )
*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationTemplates](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationTemplates )
*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues )
*  [SoftLayer_Monitoring_Agent::getGraph](/reference/services/SoftLayer_Monitoring_Agent/getGraph )



### Error Handling

* SoftLayer_Exception 

> 'You must provide an array of modified configuration value objects.' 

* SoftLayer_Exception 

> 'Your monitoring agent <monitoringAgentName> is inactive.' 

* SoftLayer_Exception 

> 'New configuration value requires a configuration definition id.' 

* SoftLayer_Exception 

> 'Configuration value already exists for {definitionName}.' 

* SoftLayer_Exception 

> 'Configuration definition cannot be found by id of {configurationDefinitionIdentifier}' 

* SoftLayer_Exception 

> 'You must provide a profile ID in a value object when adding a new value for"{sectionName}" section.' 

* SoftLayer_Exception 

> 'Cannot modify configuration profile value.' 

* SoftLayer_Exception_Public 

> 'You cannot modify the value of "{definitionName}".' 

* SoftLayer_Exception 

> 'No change has been made.' 

* SoftLayer_Exception_Public 

> 'Access Denied. "Manage Server Monitoring" is required.' 

* SoftLayer_Exception_Public 

> 'Access Denied. "Manage Virtual Server Monitoring" is required.' 

* SoftLayer_Exception_Public 

> '<monitoringAgent> does not have an active billing item.' 

* SoftLayer_Exception_Public 

> 'Hardware {fullyQualifiedDomainName} has an active transaction 
#{transactionIdentifier}' 

* SoftLayer_Exception_Public 

> 'Virtual Server {fullyQualifiedDomainName} has an active transaction 
#{transactionIdentifier}' 

* SoftLayer_Exception 

> '{configurationDefinitionName} must be set based on {configurationDefinitionName}' is thrown if an invalid configuration value is provided. 

* SoftLayer_Exception 

> 'Host name cannot be found in {value}' is thrown if a host is not found. 

* SoftLayer_Exception 

> '{definitionName} requires an IP or a host name belongs to your server or clouding instance.' 

* SoftLayer_Exception 

> 'Invalid IP address or host name' 

* SoftLayer_Exception 

> 'Received unexpected result from server.' 

* SoftLayer_Exception 

> 'Failed to retrieve resource specific data.' 

* SoftLayer_Exception_Public 

> '{definitionName} requires a valid URL starts with http:// or https://' 

* SoftLayer_Exception_Public 

> '{definitionName} requires a valid host name.' 

* SoftLayer_Exception_Public 

> '{definitionName} requires a valid host name that contains only alphanumeric characters, dashes, dots, or underscores.' 

* SoftLayer_Exception_Public 

> 'A configuration value must belong to a configuration definition.' 

* SoftLayer_Exception_Public 

> '{definitionName} requires {definitionTypeName} value.' 

* SoftLayer_Exception_Public 

> '{definitionName} requires a value listed in {definitionEnumerationValues}' 

* SoftLayer_Exception_Public 

> '{definitionName} must be equal or larger than {definitionMinimumValue}' 

* SoftLayer_Exception_Public 

> '{definitionName} must be equal or smaller than {definitionMaximumValue}' 

* SoftLayer_Exception_Public 

> 'This configuration section requires pre-config testing but the pre-testing configuration is not complete.' 

* SoftLayer_Exception_Public 

> 'Failed to perform pre-configuration test. Not all valid parameters are defined. Contact development for further assistance.' 

* SoftLayer_Exception_Public 

> 'Configuration definition {definitionName} is a required field.' 

* SoftLayer_Exception_Public 

> 'Failed to add new configuration. {preConfigurationTestErrorMessageValue|errorMessage}' 



