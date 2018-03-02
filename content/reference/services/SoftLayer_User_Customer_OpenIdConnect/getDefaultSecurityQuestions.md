---
title: "getDefaultSecurityQuestions"
description: "<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong>"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::getDefaultSecurityQuestions
## Overview 
<strong>This method is deprecated.  Please see documentation for initiatePortalPasswordChange</strong> 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|key| string| A password recovery hash key retrieved from an email sent by the [[SoftLayer_User_Customer::lostPassword|lostPassword]] method.|


### Required Headers

### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question[] </a>


### associatedMethods

*  [SoftLayer_User_Customer::lostPassword](/reference/services/SoftLayer_User_Customer/lostPassword )
*  [SoftLayer_User_Customer::setPasswordFromLostPasswordRequest](/reference/services/SoftLayer_User_Customer/setPasswordFromLostPasswordRequest )

