---
title: "restartMonitoringAgent"
description: "This method restarts a monitoring agent and sets the agent's status to 'ACTIVE'."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/restartMonitoringAgent"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::restartMonitoringAgent

This method restarts a monitoring agent.


## Overview 
This method restarts a monitoring agent and sets the agent's status to 'ACTIVE'. 

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

*  [SoftLayer_Monitoring_Agent::activate](/reference/services/SoftLayer_Monitoring_Agent/activate )
*  [SoftLayer_Monitoring_Agent::deactivate](/reference/services/SoftLayer_Monitoring_Agent/deactivate )



### Error Handling

* SoftLayer_Exception 

> Throws 'Failed to restart the monitoring agent. Please contact development.' if an error occurred when restarting the SoftLayer_Monitoring_Agent. 



