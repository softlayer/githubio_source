---
title: "initiatePortalPasswordChangeByBrandAgent"
description: "A Brand Agent that has permissions to Add Customer Accounts will be able to request the password email be sent to the Ma... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::initiatePortalPasswordChangeByBrandAgent
## Overview 
A Brand Agent that has permissions to Add Customer Accounts will be able to request the password email be sent to the Master User of a Customer Account created by the same Brand as the agent making the request. Due to security reasons, the number of reset requests are limited within an undisclosed timeframe. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username of the user to receive the password reset email|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean
