---
title: "createMxRecord"
description: "Create an MX record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLayer... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::createMxRecord

Create an MX record on a domain.


## Overview 
Create an MX record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLayer_Dns_Domain_ResourceRecord if you already have a domain record available. MX records are created with a default priority of 10. createMxRecord returns the newly created SoftLayer_Dns_Domain_ResourceRecord_MxType. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|host| string| The resource record's name|
|data| string| The resource record's value|
|ttl| integer| The resource record's time-to-live value.|
|mxPriority| integer| The priority this MX record has for mail delivery. Lower priority MTAs are contacted first.|


### Required Headers
* authenticate
* SoftLayer_Dns_DomainInitParameters

### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType'>SoftLayer_Dns_Domain_ResourceRecord_MxType </a>

### External Links


* [MX record at Wikipedia](http://en.wikipedia.org/wiki/MX_record)


