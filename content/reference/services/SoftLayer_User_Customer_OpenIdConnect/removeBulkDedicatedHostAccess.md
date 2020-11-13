---
title: "removeBulkDedicatedHostAccess"
description: "Revokes access for the user to one or more dedicated host devices.  The user will only be allowed to see and access devi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/removeBulkDedicatedHostAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::removeBulkDedicatedHostAccess

Revoke access for the user for one or more dedicated hosts devices.


## Overview 
Revokes access for the user to one or more dedicated host devices.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access or the access has been revoked, then "not found" exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

If the user has full dedicatedHost access, then it will provide access to "ALL but passed in" dedicatedHost ids. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostIds| array of integers| Dedicated Host IDs|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess )
*  [SoftLayer_User_Customer::addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny Master User device access." when trying to remove dedicated host access to a master user. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny yourself device access." when trying to remove dedicated host access to the user making the call to the SoftLayer API. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You may not grant or deny device access to other users." when trying to remove dedicated host access the user making the API call is not their account's master user or does not have the "USER_MANAGE" portal permission. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a valid dedicated host id." if the given dedicated host id is not a valid dedicated host id. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to remove user dedicated host access." if the API was unable to remove dedicated host access from the given portal user. 



