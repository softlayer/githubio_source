---
title: "resetExpiredPassword"
description: "<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> Attempt to authen... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::resetExpiredPassword
## Overview 
<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> Attempt to authenticate a username and password to the SoftLayer customer portal and reset there password. If authentication and password reset is successful then the API returns true. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username you wish to authenticate.|
|password| string| Your SoftLayer customer portal user's portal password.|
|newPassword| string| Your new customer portal user's portal password.|
|securityQuestionId| integer| A security question you wish to answer when authenticating to the SoftLayer customer portal. This parameter isn't required if no security questions are set on your portal account or if your account is configured to not require answering a security account upon login.|
|securityQuestionAnswer| string| The answer to your security question.|


### Required Headers

### Optional Headers

### Return Values
boolean
