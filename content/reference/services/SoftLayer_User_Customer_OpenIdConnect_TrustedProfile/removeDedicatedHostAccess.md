---
title: "removeDedicatedHostAccess"
description: "Revokes access for the user to a single dedicated host device.  The user will only be allowed to see and access devices... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/removeDedicatedHostAccess"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::removeDedicatedHostAccess

Revoke access for the user to a single dedicated hosts device.


## Overview 
Revokes access for the user to a single dedicated host device.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access or the access has been revoked, then "not found" exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostId| integer| DedicatedHost ID|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess )
*  [SoftLayer_User_Customer::addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess )



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



