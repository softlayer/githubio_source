---
title: "getSoaResourceRecord"
description: "Retrieve the start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This propert... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
aliases:
    - "/reference/services/softlayer_dns_domain/getSoaResourceRecord"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::getSoaResourceRecord

Retrieve the start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject.


## Overview 
Retrieve the start of authority (SOA) record contains authoritative and propagation details for a DNS zone. This property is not considered in requests to createObject and editObject.

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
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType'>SoftLayer_Dns_Domain_ResourceRecord_SoaType </a>

