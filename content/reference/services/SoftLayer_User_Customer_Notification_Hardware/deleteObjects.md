---
title: "deleteObjects"
description: "Like any other API object, the customer notification objects can be deleted by passing an instance of them into this fun... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Hardware"
aliases:
    - "/reference/services/softlayer_user_customer_notification_hardware/deleteObjects"
---
# [SoftLayer_User_Customer_Notification_Hardware](/reference/services/SoftLayer_User_Customer_Notification_Hardware)::deleteObjects

Delete a group of Customer_Notification_Hardware objects by passing in a collection of them


## Overview 
Like any other API object, the customer notification objects can be deleted by passing an instance of them into this function.  The ID on the object must be set. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a>| An array of skeleton SoftLayer_User_Customer_Notification_Hardware objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

