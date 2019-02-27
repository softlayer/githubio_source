---
title: "removeAllAlarmSubscribers"
description: "Use of this method will allow removing all subscribers from the monitoring agent. The agent subscribers can be managed w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/removeAllAlarmSubscribers"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::removeAllAlarmSubscribers

Removes all users from receiving the alarms for this monitoring agent.


## Overview 
Use of this method will allow removing all subscribers from the monitoring agent. The agent subscribers can be managed within the portal from the "Alarm Subscribers" tab of the monitoring agent configuration. 

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

*  [SoftLayer_Monitoring_Agent::getEligibleAlarmSubscibers](/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers )
*  [SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber )
*  [SoftLayer_Monitoring_Agent::removeActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/removeActiveAlarmSubscriber )
*  [SoftLayer_Monitoring_Agent::getActiveAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/getActiveAlarmSubscribers )




