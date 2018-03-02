---
title: "createPtrRecord"
description: "setPtrRecordForIpAddress() sets a single reverse DNS record for a single IP address and returns the newly created or edi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
---
# SoftLayer_Dns_Domain::createPtrRecord
## Overview 
setPtrRecordForIpAddress() sets a single reverse DNS record for a single IP address and returns the newly created or edited [[SoftLayer_Dns_Domain_ResourceRecord]] record. Currently this method only supports IPv4 addresses and performs no operation when given an IPv6 address. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IP address whose PTR record you wish to set.|
|ptrRecord| string| The PTR record you wish to set.|
|ttl| integer| The time-to-live value of the PTR record.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord </a>

