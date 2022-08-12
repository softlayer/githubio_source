---
title: "turnOffMasterUserPermissionCheckMode"
description: "This method allows the master user of an account to undo the designation of this user as an alternate master user.  This can not be applied to the true master user of the account. 

Note that this method, by itself, WILL NOT affect the IAM Policies granted this user.  This API is not intended for general customer use.  It is intended to be called by IAM, in concert with other actions taken by IAM when the master user / account owner turns off an 'alternate/auxiliary master user / account owner'. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
---
