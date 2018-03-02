---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain object whose ID number corresponds to the ID number of the init parameter p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
---
# SoftLayer_Dns_Domain::getObject
## Overview 
getObject retrieves the SoftLayer_Dns_Domain object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain service. You can only retrieve domains that are assigned to your SoftLayer account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Dns_DomainInitParameters
* authenticate

### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_Dns_DomainObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>

