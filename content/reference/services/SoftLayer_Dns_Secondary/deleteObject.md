---
title: "deleteObject"
description: "Delete a secondary DNS Record. This will also remove any associated domain records and resource records on the SoftLayer... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---
# SoftLayer_Dns_Secondary::deleteObject
## Overview 
Delete a secondary DNS Record. This will also remove any associated domain records and resource records on the SoftLayer nameservers that were created as a result of the zone transfers. This action cannot be undone. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_SecondaryInitParameters

### Optional Headers

### Return Values
boolean
