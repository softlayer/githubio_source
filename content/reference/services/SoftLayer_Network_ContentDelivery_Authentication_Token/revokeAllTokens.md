---
title: "revokeAllTokens"
description: "This method revokes all tokens belong to a CDN account.  Valid media types are 'HTTP', 'FLASH' and 'WM'."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Token"
---
# SoftLayer_Network_ContentDelivery_Authentication_Token::revokeAllTokens
## Overview 
This method revokes all tokens belong to a CDN account.  Valid media types are "HTTP", "FLASH" and "WM". 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|cdnAccountId| integer| A CDN account Id|
|mediaType| string| Media type you wish to revoke tokens for|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean
