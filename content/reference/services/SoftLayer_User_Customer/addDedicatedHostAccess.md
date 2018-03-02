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
---
# SoftLayer_User_Customer::addDedicatedHostAccess
## Overview 
Grants the user access to a single dedicated host device.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access, then "not found" exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostId| integer| The identifier of the dedicatedHost to add to a user's dedicatedHost access list.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess )

