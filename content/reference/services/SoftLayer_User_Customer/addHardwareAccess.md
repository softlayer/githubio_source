---
title: "addHardwareAccess"
description: "Add hardware to a portal user's hardware access list. A user's hardware access list controls which of an account's hardw... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::addHardwareAccess
## Overview 
Add hardware to a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. Hardware does not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user already has access to the hardware you're attempting to add then addHardwareAccess() returns true. 

Users can assign hardware access to their child users, but not to themselves. An account's master has access to all hardware on their customer account and can set hardware access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The identifier of the hardware to add to a user's hardware access list.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess )
*  [SoftLayer_User_Customer::removeHardwareAccess](/reference/services/SoftLayer_User_Customer/removeHardwareAccess )
*  [SoftLayer_User_Customer::removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess )

