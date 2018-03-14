---
title: "removeHardwareAccess"
description: "Remove hardware from a portal user's hardware access list. A user's hardware access list controls which of an account's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/removeHardwareAccess"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::removeHardwareAccess

Remove hardware from a portal user's hardware access list.


## Overview 
Remove hardware from a portal user's hardware access list. A user's hardware access list controls which of an account's hardware objects a user has access to in the SoftLayer customer portal and API. Hardware does not exist in the SoftLayer portal and returns "not found" exceptions in the API if the user doesn't have access to it. If a user does not has access to the hardware you're attempting remove add then removeHardwareAccess() returns true. 

Users can assign hardware access to their child users, but not to themselves. An account's master has access to all hardware on their customer account and can set hardware access for any of the other users on their account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| Hardware ID|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::addHardwareAccess](/reference/services/SoftLayer_User_Customer/addHardwareAccess )
*  [SoftLayer_User_Customer::addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess )
*  [SoftLayer_User_Customer::removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess )

