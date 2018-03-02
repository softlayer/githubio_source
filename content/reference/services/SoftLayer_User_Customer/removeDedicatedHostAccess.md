---
title: "removeDedicatedHostAccess"
description: "Revokes access for the user to a single dedicated host device.  The user will only be allowed to see and access devices... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::removeDedicatedHostAccess
## Overview 
Revokes access for the user to a single dedicated host device.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access or the access has been revoked, then "not found" exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostId| integer| DedicatedHost ID|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess )
*  [SoftLayer_User_Customer::addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess )

