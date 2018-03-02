---
title: "addBulkDedicatedHostAccess"
description: "Grants the user access to one or more dedicated host devices.  The user will only be allowed to see and access devices i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::addBulkDedicatedHostAccess
## Overview 
Grants the user access to one or more dedicated host devices.  The user will only be allowed to see and access devices in both the portal and the API to which they have been granted access.  If the user's account has devices to which the user has not been granted access, then "not found" exceptions are thrown if the user attempts to access any of these devices. 

Users can assign device access to their child users, but not to themselves. An account's master has access to all devices on their customer account and can set dedicated host access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHostIds| array of integers| Dedicated Host IDs|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess )
*  [SoftLayer_User_Customer::removeDedicatedHostAcces](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAcces )
*  [SoftLayer_User_Customer::removeBulkHDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkHDedicatedHostAccess )

