---
title: "createSpfRecord"
description: "Create an SPF record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLaye... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
aliases:
    - "/reference/services/softlayer_dns_domain/createSpfRecord"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::createSpfRecord

Create an SPF record on a domain.


## Overview 
Create an SPF record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLayer_Dns_Domain_ResourceRecord if you already have a domain record available. createARecord returns the newly created SoftLayer_Dns_Domain_ResourceRecord_SpfType. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SpfType'>SoftLayer_Dns_Domain_ResourceRecord_SpfType </a>

### External Links


* [List of DNS record types at Wikipedia](http://en.wikipedia.org/wiki/List_of_DNS_record_types)


* [Sender Policy Framework](http://www.openspf.org/Project_Overview)





