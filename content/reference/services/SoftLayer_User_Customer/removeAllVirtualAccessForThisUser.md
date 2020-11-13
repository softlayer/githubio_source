---
title: "removeAllVirtualAccessForThisUser"
description: "Remove all cloud computing instances from a portal user's instance access list. A user's instance access list controls w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/removeAllVirtualAccessForThisUser"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::removeAllVirtualAccessForThisUser

Remove all cloud computing instances from a portal user's instance access list.


## Overview 
Remove all cloud computing instances from a portal user's instance access list. A user's instance access list controls which of an account's computing instance objects a user has access to in the SoftLayer customer portal and API. If the current user does not have administrative privileges over this user, an inadequate permissions exception will get thrown. 

Users can call this function on child users, but not to themselves. An account's master has access to all users permissions on their account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess )
*  [SoftLayer_User_Customer::addBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess )
*  [SoftLayer_User_Customer::removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception if the active user is not the master user or the parent of this user. 



