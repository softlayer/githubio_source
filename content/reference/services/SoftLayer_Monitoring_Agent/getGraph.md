---
title: "getGraph"
description: "This method returns a SoftLayer_Container_Bandwidth_GraphOutputs object containing a base64 PNG string graph of the prov... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/getGraph"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getGraph

Retrieves a graph for configuration values within the date range.


## Overview 
This method returns a SoftLayer_Container_Bandwidth_GraphOutputs object containing a base64 PNG string graph of the provided configuration values for the given begin and end dates. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationValues| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>| The configuration values to be|
|beginDate| dateTime| $beginDate           Graph start date and time|
|endDate| dateTime| $endDate             Graph end date and time|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Monitoring_Graph_Outputs'>SoftLayer_Container_Monitoring_Graph_Outputs </a>


### Associated Methods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )
*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues )



### Error Handling

* SoftLayer_Exception 

> Throws 'The configuration value supplied is not supported for metric tracking.' if for any of the configuration values provided by the user in the $configurationValues parameter, there is no SoftLayer_Configuration_Template_Section_Definition_Attribute with a SoftLayer_Configuration_Template_Section_Definition_Attribute_Type with a key name of 'MONITORING_QOS_DATA_FLAG' for the associated SoftLayer_Configuration_Template_Section_Definition. 

* SoftLayer_Exception_Public 

> Throws 'The configuration value supplied is invalid.' if for any of the configuration values provided by the user in the $configurationValues parameter, this SoftLayer_Monitoring_Agent has no associated SoftLayer_Monitoring_Agent_Configuration_Value. 

* SoftLayer_Exception_Public 

> Throws 'One of the configuration values supplied does not have the graph type defined. Please contact support for assistance.' if for any of the configuration values provided by the user in the $configurationValues parameter the associated SoftLayer_Configuration_Template_Section_Definition has no SoftLayer_Configuration_Template_Section_Definition_Attribute with a SoftLayer_Configuration_Template_Section_Definition_Attribute_Type that has a key name of 'MONITORING_QOS_TYPE_KEYNAME'. 

* SoftLayer_Exception_Public 

> Throws 'Only items with the same units can be graphed together.' if there are more than one configuration values passed in the $configurationValues parameter and they don't all contain the same metric graph template. 



