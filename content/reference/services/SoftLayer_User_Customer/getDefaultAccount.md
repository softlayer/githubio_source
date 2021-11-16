---
title: "getDefaultAccount"
description: "This method is not applicable to legacy SoftLayer-authenticated users and can only be invoked for IBMid-authenticated us... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/getDefaultAccount"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::getDefaultAccount


This method should never be invoked as it is not applicable to legacy SoftLayer-authenticated users. See SoftLayer_User_Customer_OpenIdConnect::getDefaultAccount instead. 


## Overview 
This method is not applicable to legacy SoftLayer-authenticated users and can only be invoked for IBMid-authenticated users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters


### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>




