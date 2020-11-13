---
title: "removeAllDedicatedHostAccessForThisUser"
description: "Revoke access to all dedicated hosts on the account for this user. The user will only be allowed to see and access devic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/removeAllDedicatedHostAccessForThisUser"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::removeAllDedicatedHostAccessForThisUser

Revoke access to all dedicated hosts on the account for this user.


## Overview 
Revoke access to all dedicated hosts on the account for this user. The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access or the access has been revoked, then "not found" exceptions are thrown if the user attempts to access any of these devices. If the current user does not have administrative privileges over this user, an inadequate permissions exception will get thrown. 

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

*  [SoftLayer_User_Customer::addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess )
*  [SoftLayer_User_Customer::addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Unable to remove user dedicated host access." if the API was unable to remove dedicated host access from the given portal user. 

* SoftLayer_Exception_Public 

> Throws the exception "Inadequate permissions." if the active user permissions do allow for access to the userId in question. 



