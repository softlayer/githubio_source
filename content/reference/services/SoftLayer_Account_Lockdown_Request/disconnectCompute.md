---
title: "disconnectCompute"
description: "Takes an account ID and an optional disconnect date. If no disconnect date is passed into the API call, the account disc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Lockdown_Request"
aliases:
    - "/reference/services/softlayer_account_lockdown_request/disconnectCompute"
---
# [SoftLayer_Account_Lockdown_Request](/reference/services/SoftLayer_Account_Lockdown_Request)::disconnectCompute

Disconnecting a customer will disable all hardware resources (servers and


## Overview 
Takes an account ID and an optional disconnect date. If no disconnect date is passed into the API call, the account disconnection will happen immediately. Otherwise, the account disconnection will happen on the date given. A brand account request ID will be returned and will then be updated when the disconnection occurs. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|accountId| integer| |
|disconnectDate| string| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
integer

