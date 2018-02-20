---
title: "updatePassword"
description: "<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> Update a user's p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::updatePassword
## Overview 
<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> Update a user's password on the SoftLayer customer portal. As with forum passwords, user portal passwords must match the following restrictions. Portal passwords must... 
* ...be over eight characters long.
* ...be under twenty characters long.
* ...contain at least one uppercase letter
* ...contain at least one lowercase letter
* ...contain at least one number
* ...contain one of the special characters _ - | @ . , ? / ! ~ # $ % ^ & * ( ) { } [ ] \ + =
* ...not match your username
* ...not match your forum password
Finally, users can only update their own password. An account's master user can update any of their account users' passwords. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|password| string| Your new portal password|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean
