---
title: "addApiAuthenticationKey"
description: "Create a user's API authentication key, allowing that user access to query the SoftLayer API. addApiAuthenticationKey()... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/addApiAuthenticationKey"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::addApiAuthenticationKey

Create a user's API authentication key.


## Overview 
Create a user's API authentication key, allowing that user access to query the SoftLayer API. addApiAuthenticationKey() returns the user's new API key. Each portal user is allowed only one API key. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters


### Return Values
* string


### Associated Methods

*  [SoftLayer_User_Customer::removeApiAuthenticationKey](/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception <<< EOT 



