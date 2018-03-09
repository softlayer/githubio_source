---
title: "createCnameRecord"
description: "Create a CNAME record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLay... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::createCnameRecord

Create a CNAME record on a domain.


## Overview 
Create a CNAME record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLayer_Dns_Domain_ResourceRecord if you already have a domain record available. createCnameRecord returns the newly created SoftLayer_Dns_Domain_ResourceRecord_CnameType. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|host| string| The resource record's name|
|data| string| The resource record's value|
|ttl| integer| The resource record's time-to-live value.|


### Required Headers
* authenticate
* SoftLayer_Dns_DomainInitParameters

### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_CnameType'>SoftLayer_Dns_Domain_ResourceRecord_CnameType </a>

### External Links


* [List of DNS record types at Wikipedia](http://en.wikipedia.org/wiki/List_of_DNS_record_types)


