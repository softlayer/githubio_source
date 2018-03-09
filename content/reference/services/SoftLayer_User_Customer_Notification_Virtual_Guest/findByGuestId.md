---
title: "findByGuestId"
description: "This method returns all SoftLayer_User_Customer_Notification_Virtual_Guest objects associated with the passed in ID as l... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
---
# [SoftLayer_User_Customer_Notification_Virtual_Guest](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest)::findByGuestId

Return all CloudLayer computing instance notifications associated with the passed ID


## Overview 
This method returns all SoftLayer_User_Customer_Notification_Virtual_Guest objects associated with the passed in ID as long as that hardware ID is owned by the current user's account. 

This behavior can also be accomplished by simply tapping monitoringUserNotification on the Virtual_Guest object. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|id| integer| The ID of the CloudLayer computing instance (virtual_guest) object to search by.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_User_Customer_Notification_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest'>SoftLayer_User_Customer_Notification_Virtual_Guest[] </a>

