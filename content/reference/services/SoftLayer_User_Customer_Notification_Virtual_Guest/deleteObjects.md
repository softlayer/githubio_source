---
title: "deleteObjects"
description: "Like any other API object, the customer notification objects can be deleted by passing an instance of them into this fun... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
---
# [SoftLayer_User_Customer_Notification_Virtual_Guest](/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest)::deleteObjects

Delete a group of SoftLayer_Customer_Notification_Virtual_Guest objects by passing in a collection of them


## Overview 
Like any other API object, the customer notification objects can be deleted by passing an instance of them into this function.  The ID on the object must be set. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest'>SoftLayer_User_Customer_Notification_Virtual_Guest[] </a>| An array of skeleton SoftLayer_User_Customer_Notification_Virtual_Guest objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

