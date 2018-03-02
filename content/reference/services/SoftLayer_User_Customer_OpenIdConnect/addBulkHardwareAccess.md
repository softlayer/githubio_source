---
title: "addBulkHardwareAccess"
description: "Add multiple hardware to a portal user's hardware access list. A user's hardware access list controls which of an accoun... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::addBulkHardwareAccess
## Overview 
Add multiple hardware to a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. Hardware does not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. addBulkHardwareAccess() does not attempt to add hardware access if the given user already has access to that hardware object. 

Users can assign hardware access to their child users, but not to themselves. An account's master has access to all hardware on their customer account and can set hardware access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareIds| array of integers| Hardware IDs|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addHardwareAccess](/reference/services/SoftLayer_User_Customer/addHardwareAccess )
*  [SoftLayer_User_Customer::removeHardwareAccess](/reference/services/SoftLayer_User_Customer/removeHardwareAccess )
*  [SoftLayer_User_Customer::removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess )

