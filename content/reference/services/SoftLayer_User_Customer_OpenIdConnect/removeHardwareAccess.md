---
title: "removeHardwareAccess"
description: "Remove hardware from a portal user's hardware access list. A user's hardware access list controls which of an account's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/removeHardwareAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::removeHardwareAccess

Remove hardware from a portal user's hardware access list.


## Overview 
Remove hardware from a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. Hardware does not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user does not has access to the hardware you're attempting remove add then removeHardwareAccess() returns true. 

Users can assign hardware access to their child users, but not to themselves. An account's master has access to all hardware on their customer account and can set hardware access for any of the other users on their account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| Hardware ID|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addHardwareAccess](/reference/services/SoftLayer_User_Customer/addHardwareAccess )
*  [SoftLayer_User_Customer::addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess )
*  [SoftLayer_User_Customer::removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throw the exception "You may not grant or deny Master User device access." when trying to remove hardware access to a master user. 

* SoftLayer_Exception_PermissionDenied 

> Throw the exception "You may not grant or deny yourself device access." when trying to remove hardware access to the user making the call to the SoftLayer API. 

* SoftLayer_Exception_PermissionDenied 

> Throw the exception "You may not grant or deny device access to other users." when trying to remove hardware access the user making the API call is not their account's master user or does not have the "USER_MANAGE" portal permission. 

* SoftLayer_Exception_Public 

> Throw the exception "Please specify a valid hardware id." if the given hardware id is not a valid hardware id. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to remove user hardware access." if the API was unable to remove hardware access from the given portal user. 



