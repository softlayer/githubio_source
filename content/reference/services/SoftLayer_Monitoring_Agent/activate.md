---
title: "activate"
description: "This method activates a SoftLayer_Monitoring_Agent."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/activate"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::activate

Activates a monitoring agent


## Overview 
This method activates a SoftLayer_Monitoring_Agent.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Monitoring_Agent::restart](/reference/services/SoftLayer_Monitoring_Agent/restart )
*  [SoftLayer_Monitoring_Agent::deactivate](/reference/services/SoftLayer_Monitoring_Agent/deactivate )



### Error Handling

* SoftLayer_Exception 

> Throws 'Failed to activate monitoring agent "{monitoringAgentName}".' if an error occurred while trying to activate the SoftLayer_Monitoring_Agent and the active user is an instance of SoftLayer_User_Interface. 



