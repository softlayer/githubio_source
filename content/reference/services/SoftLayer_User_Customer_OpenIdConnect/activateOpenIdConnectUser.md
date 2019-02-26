---
title: "activateOpenIdConnectUser"
description: "Completes invitation process for an OpenIdConnect user created by Bluemix Unified User Console."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/activateOpenIdConnectUser"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::activateOpenIdConnectUser

Completes invitation process for an OIDC user initiated by the


## Overview 
Completes invitation process for an OpenIdConnect user created by Bluemix Unified User Console. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|verificationCode| string| : invitation code used to create the user|
|userInfo| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>| : user object fields to be updated|
|iamId| string| Fully qualified (realm-id format) IAMid for the user (optional)|


### Required Headers


### Return Values
* void



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Error completing activation." if there was an error completing activation. 



