---
title: "getActiveAlarms"
description: "Return all currently active alarms on this account.  Only alarms on hardware and virtual servers accessible to the curre... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getActiveAlarms"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getActiveAlarms

Get all active alarms on this account.


## Overview 
Return all currently active alarms on this account.  Only alarms on hardware and virtual servers accessible to the current user will be returned. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Monitoring_Alarm_History'>SoftLayer_Container_Monitoring_Alarm_History[] </a>




