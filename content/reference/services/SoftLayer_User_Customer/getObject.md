---
title: "getObject"
description: "getObject retrieves the SoftLayer_User_Customer object whose ID number corresponds to the ID number of the init paramete... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/getObject"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::getObject

Retrieve a SoftLayer_User_Customer record.


## Overview 
getObject retrieves the SoftLayer_User_Customer object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_User_Customer service. You can only retrieve users that are assigned to the customer account belonging to the user making the API call. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_CustomerInitParameters
* authenticate


### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_User_CustomerObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> <<< EOT 

* SoftLayer_Exception_AccessDenied 

> <<< EOT 



