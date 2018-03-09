---
title: "findByHardwareId"
description: "This method returns all Customer_Notification_Hardware objects associated with the passed in hardware ID as long as that... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Hardware"
---
# [SoftLayer_User_Customer_Notification_Hardware](/reference/services/SoftLayer_User_Customer_Notification_Hardware)::findByHardwareId

Return all hardware notifications associated with the passed hardware ID


## Overview 
This method returns all Customer_Notification_Hardware objects associated with the passed in hardware ID as long as that hardware ID is owned by the current user's account. 

This behavior can also be accomplished by simply tapping monitoringUserNotification on the Hardware_Server object. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The ID of the hardware object to search by.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_User_Customer_Notification_HardwareObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a>

