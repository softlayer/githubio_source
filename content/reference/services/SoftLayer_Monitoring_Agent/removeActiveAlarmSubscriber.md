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
aliases:
    - "/reference/services/softlayer_monitoring_agent/removeActiveAlarmSubscriber"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::removeActiveAlarmSubscriber

Removes the selected user from receiving the alarms for this monitoring agent. 


## Overview 
Use of this method will allow removing active subscribers from the monitoring agent. The agent subscribers can be managed within the portal from the "Alarm Subscribers" tab of the monitoring agent configuration. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|userRecordId| integer| A valid numeric SoftLayer_User_Customer::id for a user on your account to be removed|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Monitoring_Agent::getEligibleAlarmSubscibers](/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers )
*  [SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber )
*  [SoftLayer_Monitoring_Agent::removeAllAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/removeAllAlarmSubscribers )
*  [SoftLayer_Monitoring_Agent::getActiveAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/getActiveAlarmSubscribers )



### Error Handling

* SoftLayer_Exception_Public 

> Throws 'You do not have permission to set this user as an alarm messages recipient.' if no SoftLayer_User_Customer is found, using the provided $userRecordId, associated with the active user's account. 



