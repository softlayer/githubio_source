---
title: "removeAllHardwareAccessForThisUser"
description: "Remove all hardware from a portal user's hardware access list. A user's hardware access list controls which of an accoun... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/removeAllHardwareAccessForThisUser"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::removeAllHardwareAccessForThisUser


Remove all hardware from a portal user's hardware access list.


## Overview 
Remove all hardware from a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. If the current user does not have administrative privileges over this user, an inadequate permissions exception will get thrown. 

Users can call this function on child users, but not to themselves. An account's master has access to all users permissions on their account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addHardwareAccess](/reference/services/SoftLayer_User_Customer/addHardwareAccess )
*  [SoftLayer_User_Customer::addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess )
*  [SoftLayer_User_Customer::removeHardwareAccess](/reference/services/SoftLayer_User_Customer/removeHardwareAccess )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Unable to remove user hardware access." if the API was unable to remove hardware access from the given portal user. 

* SoftLayer_Exception_Public 

> Throws the exception "Inadequate permissions." if the active user permissions do allow for access to the userId in question. 



