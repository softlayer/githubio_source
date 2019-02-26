---
title: "getByDomainName"
description: "Search for [[SoftLayer_Dns_Domain]] records by domain name. getByDomainName() performs an inclusive search for domain re... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
aliases:
    - "/reference/services/softlayer_dns_domain/getByDomainName"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::getByDomainName

Search for domains by name.


## Overview 
Search for [[SoftLayer_Dns_Domain]] records by domain name. getByDomainName() performs an inclusive search for domain records, returning multiple records based on partial name matches. Use this method to locate domain records if you don't have access to their id numbers. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|name| string| The portion of the domain name you wish to search for.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Dns_DomainObjectFilter

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>




