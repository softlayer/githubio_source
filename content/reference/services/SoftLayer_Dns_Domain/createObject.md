---
title: "createObject"
description: "Create a new domain on the SoftLayer name servers. The SoftLayer_Dns_Domain object passed to this function must have at... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
aliases:
    - "/reference/services/softlayer_dns_domain/createObject"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::createObject

Create a new domain.


## Overview 
Create a new domain on the SoftLayer name servers. The SoftLayer_Dns_Domain object passed to this function must have at least one A or AAAA resource record. 

createObject creates a default SOA record with the data: 
* '''host''': "@"
* '''data''': "ns1.softlayer.com."
* '''responsible person''': "root.[your domain name]."
* '''expire''': 604800 seconds
* '''refresh''': 3600 seconds
* '''retry''': 300 seconds
* '''minimum''': 3600 seconds


If your new domain uses the .de top-level domain then SOA refresh is set to 10000 seconds, retry is set to 1800 seconds, and minimum to 10000 seconds. 

If your domain doesn't contain NS resource records for ns1.softlayer.com or ns2.softlayer.com then ''createObject'' will create them for you. 

''createObject'' returns a Boolean ''true'' on successful object creation or ''false'' if your domain was unable to be created.. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>| The SoftLayer_Dns_Domain object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain </a>


### Associated Methods

*  [SoftLayer_Dns_Domain::createObjects](/reference/services/SoftLayer_Dns_Domain/createObjects )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "At least one valid 'A' or 'AAAA' resource record is required to create a domain." if the domain in the templateObject parameter doesn't have at least one A or AAAA resource record. 



