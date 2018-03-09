---
title: "disableLockedAccount"
description: "Takes the original lockdown request ID, and an optional disable date. If no date is passed with the API call, the accoun... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Lockdown_Request"
---
# [SoftLayer_Account_Lockdown_Request](/reference/services/SoftLayer_Account_Lockdown_Request)::disableLockedAccount

Disabling an account is a PERMANENT action. All billable items under the


## Overview 
Takes the original lockdown request ID, and an optional disable date. If no date is passed with the API call, the account will be disabled immediately. Otherwise, the account will be disabled on the date given. All hardware will be reclaimed and all accounts permanently disabled. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|disableDate| string| |


### Required Headers
* authenticate
* SoftLayer_Account_Lockdown_RequestInitParameters

### Optional Headers

### Return Values
integer

