---
title: "revokeManagedToken"
description: "This method is deprecated! 

Revokes a managed token. If you revoke a token, the token will be removed from SoftLayer's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Token"
---
# [SoftLayer_Network_ContentDelivery_Authentication_Token](/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token)::revokeManagedToken

(DEPRECATED) Revokes a managed token


## Overview 
This method is deprecated! 

Revokes a managed token. If you revoke a token, the token will be removed from SoftLayer's system but it will not remove your content on CDN FTP. The content that requires token validation will not be available to the visitor who is using a revoked token. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|cdnAccountId| integer| A CDN account id|
|token| string| A managed authentication token|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

