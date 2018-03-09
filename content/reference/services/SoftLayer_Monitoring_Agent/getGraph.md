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
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getGraph

Retrieves a graph for configuration values within the date range.


## Overview 
This method returns a SoftLayer_Container_Bandwidth_GraphOutputs object containing a base64 PNG string graph of the provided configuration values for the given begin and end dates. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationValues| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>| The configuration values to be|
|beginDate| dateTime| $beginDate           Graph start date and time|
|endDate| dateTime| $endDate             Graph end date and time|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Monitoring_Graph_Outputs'>SoftLayer_Container_Monitoring_Graph_Outputs </a>


### associatedMethods

*  [SoftLayer_Monitoring_Agent::addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile )
*  [SoftLayer_Monitoring_Agent::applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues )
*  [SoftLayer_Monitoring_Agent::getAvailableConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues )

