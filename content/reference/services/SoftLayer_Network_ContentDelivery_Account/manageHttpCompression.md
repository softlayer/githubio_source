---
title: "manageHttpCompression"
description: "HTTP Compression is used to reduce the bandwidth used to deliver an object. You can specify list of content types that n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::manageHttpCompression
## Overview 
HTTP Compression is used to reduce the bandwidth used to deliver an object. You can specify list of content types that needs to be compressed. If you omit the content type parameter, these values will be used by default: 
* text/plain
* text/html
* text/css
* application/x-javascript
* text/javascript


Note that files larger than 1MB will never be served with compression regardless of whether their content-type is enabled for compression. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|enableFlag| boolean| |
|mimeTypes| array of strings| |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean

