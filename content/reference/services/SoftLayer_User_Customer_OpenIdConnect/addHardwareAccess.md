---
title: "addHardwareAccess"
description: "Add hardware to a portal user's hardware access list. A user's hardware access list controls which of an account's hardw... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/addHardwareAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::addHardwareAccess


Add hardware to a portal user's hardware access list.


## Overview 
Add hardware to a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. Hardware does not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user already has access to the hardware you're attempting to add then addHardwareAccess() returns true. 

Users can assign hardware access to their child users, but not to themselves. An account's master has access to all hardware on their customer account and can set hardware access for any of the other users on their account. 

Only the USER_MANAGE permission is required to execute this. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The identifier of the hardware to add to a user's hardware access list.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess )
*  [SoftLayer_User_Customer::removeHardwareAccess](/reference/services/SoftLayer_User_Customer/removeHardwareAccess )
*  [SoftLayer_User_Customer::removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny Master User device access." when trying to add hardware access to a master user. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny yourself device access." when trying to add hardware access to the user making the call to the SoftLayer API. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny device access to other users." when trying to add hardware access the user making the API call is not their account's master user or does not have the "USER_MANAGE" portal permission. 

* SoftLayer_Exception_Public 

> Throws the exception "You may not add hardware permissions that the parent does not possess to this account." when trying to add hardware access to the user and the parent user does not possess that access to that hardware. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a valid hardware id." if the given hardware id is not a valid hardware id. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to add user hardware access." if the API was unable to assign hardware access to the given portal user. 



