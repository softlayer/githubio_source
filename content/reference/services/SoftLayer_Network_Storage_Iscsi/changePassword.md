---
title: "changePassword"
description: "The method will change the password for the given Storage/Virtual Server Storage account."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::changePassword
## Overview 
The method will change the password for the given Storage/Virtual Server Storage account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| Username of the Storage/Virtual Server Storage account to apply the password change to|
|currentPassword| string| The current password for the account|
|newPassword| string| New Password for Storage/Virtual Server account|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean
