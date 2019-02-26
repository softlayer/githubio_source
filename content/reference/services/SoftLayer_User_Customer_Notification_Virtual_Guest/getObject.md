---
title: "getObject"
description: "getObject retrieves the SoftLayer_User_Customer_Notification_Virtual_Guest object whose ID number corresponds to the ID... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_user_customer_notification_virtual_guest/getObject"
---
# [SoftLayer_User_Customer_Notification_Virtual_Guest](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest)::getObject

Retrieve a SoftLayer_User_Customer_Notification_Virtual_Guest record.


## Overview 
getObject retrieves the SoftLayer_User_Customer_Notification_Virtual_Guest object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_User_Customer_Notification_Virtual_Guest service. You can only retrieve guest notifications attached to virtual guests and users that belong to your account 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_Customer_Notification_Virtual_GuestInitParameters
* authenticate


### Optional Headers
* SoftLayer_User_Customer_Notification_Virtual_GuestObjectMask
* SoftLayer_User_Customer_Notification_Virtual_GuestObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest'>SoftLayer_User_Customer_Notification_Virtual_Guest </a>




