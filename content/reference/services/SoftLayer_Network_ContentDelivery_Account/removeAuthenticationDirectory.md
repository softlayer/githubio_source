---
title: "removeAuthenticationDirectory"
description: "If you want to turn off the token authentication, use this method to remove a directory from the token authentication di... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::removeAuthenticationDirectory

Deletes a token authentication directory


## Overview 
If you want to turn off the token authentication, use this method to remove a directory from the token authentication directory. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|directory| string| A directory name on your CDN FTP|
|mediaType| string| Valid content types are: HTTP_LARGE, HTTP_SMALL, FLASH and WM|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean

