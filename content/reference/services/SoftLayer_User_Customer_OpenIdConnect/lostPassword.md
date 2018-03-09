---
title: "lostPassword"
description: "<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> SoftLayer provide... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::lostPassword

Generate a lost password request


## Overview 
<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> SoftLayer provides a way for users of it's customer portal to recover lost passwords. The lostPassword() method is the first step in this process. Given a valid username and email address, the SoftLayer API will email the address provided with a URL to visit to begin the password recovery process. The last part of this URL is a hash key that's used as an identifier throughout this process. Use this hash key in the [[SoftLayer_User_Customer::setPasswordFromLostPasswordRequest|setPasswordFromLostPasswordRequest]] method to reset a user's password. Password recovery hash keys are valid for 24 hours after they're generated. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username of the user whose password you wish to recover.|
|email| string| The email address of the user whose password you wish to recover. Provide the email address SoftLayer has on record for this user.|


### Required Headers

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::getUserFromLostPasswordRequest](/reference/services/SoftLayer_User_Customer/getUserFromLostPasswordRequest )
*  [SoftLayer_User_Customer::setPasswordFromLostPasswordRequest](/reference/services/SoftLayer_User_Customer/setPasswordFromLostPasswordRequest )

