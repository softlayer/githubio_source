---
title: "removeActiveAlarmSubscriber"
description: "Use of this method will allow removing active subscribers from the monitoring agent. The agent subscribers can be manage... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
---
# SoftLayer_Monitoring_Agent::removeActiveAlarmSubscriber
## Overview 
Use of this method will allow removing active subscribers from the monitoring agent. The agent subscribers can be managed within the portal from the "Alarm Subscribers" tab of the monitoring agent configuration. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|userRecordId| integer| A valid numeric SoftLayer_User_Customer::id for a user on your account to be removed|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Monitoring_Agent::getEligibleAlarmSubscibers](/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers )
*  [SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber )
*  [SoftLayer_Monitoring_Agent::removeAllAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/removeAllAlarmSubscribers )
*  [SoftLayer_Monitoring_Agent::getActiveAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/getActiveAlarmSubscribers )

