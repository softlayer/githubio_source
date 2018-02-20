---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Secondary object whose ID number corresponds to the ID number of the init paramate... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---
# SoftLayer_Dns_Secondary::getObject
## Overview 
getObject retrieves the SoftLayer_Dns_Secondary object whose ID number corresponds to the ID number of the init paramater passed to the SoftLayer_Dns_Secondary service. You can only retrieve a secondary DNS record that is assigned to your SoftLayer customer account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Dns_SecondaryInitParameters
* authenticate

### Optional Headers
* SoftLayer_Dns_SecondaryObjectMask
* SoftLayer_Dns_SecondaryObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>
