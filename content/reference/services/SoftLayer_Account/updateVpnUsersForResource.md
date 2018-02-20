---
title: "updateVpnUsersForResource"
description: "Some larger SoftLayer customer accounts may have servers and virtual servers on more subnets than SoftLayer's private ne... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::updateVpnUsersForResource
## Overview 
Some larger SoftLayer customer accounts may have servers and virtual servers on more subnets than SoftLayer's private network VPN devices can assign routes for. In those cases routes for individual servers and virtual servers may be assigned individually to an account's servers via this method. 

Always call this method to enable changes when manually configuring VPN subnet access. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|objectId| integer| The unique identifier of the hardware or computing instance you are allowing VPN access to.|
|objectType| string| The string "SoftLayer_Hardware" or "SoftLayer_Virtual_Guest" that denotes if you are allowing VPN access for a physical server or a computing instance.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean
