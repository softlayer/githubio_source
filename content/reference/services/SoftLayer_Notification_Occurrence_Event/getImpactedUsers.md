---
title: "getImpactedUsers"
description: "Retrieve a collection of users impacted by this event. Each impacted user record relates directly to a [[SoftLayer_User_... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
---
# [SoftLayer_Notification_Occurrence_Event](/reference/services/SoftLayer_Notification_Occurrence_Event)::getImpactedUsers

Retrieve a collection of users impacted by this event. Each impacted user record relates directly to a [[SoftLayer_User_Customer]].


## Overview 
Retrieve a collection of users impacted by this event. Each impacted user record relates directly to a [[SoftLayer_User_Customer]].

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
<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_User'>SoftLayer_Notification_Occurrence_User[] </a>

