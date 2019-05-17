---
title: "addDedicatedHostAccess"
description: "Grants the user access to a single dedicated host device.  The user will only be allowed to see and access devices in bo... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/addDedicatedHostAccess"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::addDedicatedHostAccess

Grant access to the user for a single dedicated host device.


## Overview 
Grants the user access to a single dedicated host device.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access, then "not found" exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

Only the USER_MANAGE permission is required to execute this. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostId| integer| The identifier of the dedicatedHost to add to a user's dedicatedHost access list.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throw the exception "You may not grant or deny Master User device access." when trying to add dedicated host access to a master user. 

* SoftLayer_Exception_PermissionDenied 

> Throw the exception "You may not grant or deny yourself device access." when trying to add dedicated host access to the user making the call to the SoftLayer API. 

* SoftLayer_Exception_PermissionDenied 

> Throw the exception "You may not grant or deny device access to other users." when trying to add dedicated host access the user making the API call is not their account's master user or does not have the "USER_MANAGE" portal permission. 

* SoftLayer_Exception_Public 

> Throw the exception "You may not add dedicated host permissions that the parent does not possess to this account." when trying to add dedicated host access to the user and the parent user does not possess access. 

* SoftLayer_Exception_Public 

> Throw the exception "Please specify a valid dedicated host id." if the given dedicated host id is not valid. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to add user dedicated host access." if the API was unable to assign dedicated host access to the given portal user. 



