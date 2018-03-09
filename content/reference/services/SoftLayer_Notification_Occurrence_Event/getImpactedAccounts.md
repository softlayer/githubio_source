---
title: "getImpactedAccounts"
description: "Retrieve a collection of accounts impacted by this event. Each impacted account record relates directly to a [[SoftLayer... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
---
# [SoftLayer_Notification_Occurrence_Event](/reference/services/SoftLayer_Notification_Occurrence_Event)::getImpactedAccounts

Retrieve a collection of accounts impacted by this event. Each impacted account record relates directly to a [[SoftLayer_Account]].


## Overview 
Retrieve a collection of accounts impacted by this event. Each impacted account record relates directly to a [[SoftLayer_Account]].

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Notification_Occurrence_EventInitParameters
* authenticate

### Optional Headers
* SoftLayer_Notification_Occurrence_EventObjectMask
* SoftLayer_Notification_Occurrence_EventObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Account'>SoftLayer_Notification_Occurrence_Account[] </a>

