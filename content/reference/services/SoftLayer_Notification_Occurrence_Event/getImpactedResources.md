---
title: "getImpactedResources"
description: "Retrieve a collection of resources impacted by this event. Each record will relate to some physical resource that the us... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
---
# SoftLayer_Notification_Occurrence_Event::getImpactedResources
## Overview 
Retrieve a collection of resources impacted by this event. Each record will relate to some physical resource that the user has access to such as [[SoftLayer_Hardware]] or [[SoftLayer_Virtual_Guest]].

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
<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource'>SoftLayer_Notification_Occurrence_Resource[] </a>

