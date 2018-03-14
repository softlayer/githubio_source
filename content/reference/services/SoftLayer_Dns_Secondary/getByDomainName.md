---
title: "getByDomainName"
description: "Search for [[SoftLayer_Dns_Domain_Secondary]] records by domain name. getByDomainName() performs an inclusive search for... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
aliases:
    - "/reference/services/softlayer_dns_secondary/getByDomainName"
---
# [SoftLayer_Dns_Secondary](/reference/services/SoftLayer_Dns_Secondary)::getByDomainName

Search for secondary domains by name.


## Overview 
Search for [[SoftLayer_Dns_Domain_Secondary]] records by domain name. getByDomainName() performs an inclusive search for secondary domain records, returning multiple records based on partial name matches. Use this method to locate secondary domain records if you don't have access to their id numbers. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|name| string| The portion of the domain name you wish to search for.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_SecondaryObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Dns_SecondaryObjectFilter

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary[] </a>

