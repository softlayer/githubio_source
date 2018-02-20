---
title: "createObjects"
description: "Create multiple SRV records on a domain. This follows the same logic as ''createObject'. The serial number of the domain... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
---
# SoftLayer_Dns_Domain_ResourceRecord_SrvType::createObjects
## Overview 
Create multiple SRV records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this SRV record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of SoftLayer_Dns_Domain_ResourceRecord objects that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecord_SrvTypeObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>
