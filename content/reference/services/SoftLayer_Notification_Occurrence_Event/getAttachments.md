---
title: "getAttachments"
description: "Retrieve a collection of attachments for this event which provide supplementary information to impacted users some examp... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
---
# SoftLayer_Notification_Occurrence_Event::getAttachments
## Overview 
Retrieve a collection of attachments for this event which provide supplementary information to impacted users some examples are RFO (Reason For Outage) and root cause analysis documents.

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
<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event_Attachment'>SoftLayer_Notification_Occurrence_Event_Attachment[] </a>
