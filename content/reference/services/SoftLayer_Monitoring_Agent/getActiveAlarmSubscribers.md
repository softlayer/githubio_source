---
title: "getActiveAlarmSubscribers"
description: "This method retrieves an array of SoftLayer_Notification_User_Subscriber objects belonging to the SoftLayer_Monitoring_A... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/getActiveAlarmSubscribers"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getActiveAlarmSubscribers

Retrieves all active users that are receiving alarm notifications.


## Overview 
This method retrieves an array of SoftLayer_Notification_User_Subscriber objects belonging to the SoftLayer_Monitoring_Agent which are able to receive alarm notifications. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>


### associatedMethods

*  [SoftLayer_Monitoring_Agent::getEligibleAlarmSubscibers](/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers )
*  [SoftLayer_Monitoring_Agent::removeActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/removeActiveAlarmSubscriber )
*  [SoftLayer_Monitoring_Agent::removeAllAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/removeAllAlarmSubscribers )
*  [SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber )

