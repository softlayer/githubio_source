---
title: "managerApprove"
description: "Applies manager approval to a pending internal IBM account request. If cost recovery is already configured, this will cr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
---
# [SoftLayer_Account_Internal_Ibm](/reference/services/SoftLayer_Account_Internal_Ibm)::managerApprove

Applies manager approval to a pending internal IBM account request


## Overview 
Applies manager approval to a pending internal IBM account request. If cost recovery is already configured, this will create an account. If not, this will remind the internal team to configure cost recovery and create the account when possible. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|requestId| integer| |
|accessToken| string| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
void

