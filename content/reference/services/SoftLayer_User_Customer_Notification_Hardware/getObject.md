---
title: "getObject"
description: "getObject retrieves the SoftLayer_User_Customer_Notification_Hardware object whose ID number corresponds to the ID numbe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Hardware"
aliases:
    - "/reference/services/softlayer_user_customer_notification_hardware/getObject"
---
# [SoftLayer_User_Customer_Notification_Hardware](/reference/services/SoftLayer_User_Customer_Notification_Hardware)::getObject

Retrieve a SoftLayer_User_Customer_Notification_Hardware record.


## Overview 
getObject retrieves the SoftLayer_User_Customer_Notification_Hardware object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_User_Customer_Notification_Hardware service. You can only retrieve hardware notifications attached to hardware and users that belong to your account 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_Customer_Notification_HardwareInitParameters
* authenticate


### Optional Headers
* SoftLayer_User_Customer_Notification_HardwareObjectMask
* SoftLayer_User_Customer_Notification_HardwareObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware </a>




