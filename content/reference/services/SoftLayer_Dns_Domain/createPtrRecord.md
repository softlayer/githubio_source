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
aliases:
    - "/reference/services/softlayer_dns_domain/createPtrRecord"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::createPtrRecord


Edit the PTR record for a single IP address.


## Overview 
setPtrRecordForIpAddress() sets a single reverse DNS record for a single IP address and returns the newly created or edited [SoftLayer_Dns_Domain_ResourceRecord]({{<ref "reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord">}}) record. Currently this method only supports IPv4 addresses and performs no operation when given an IPv6 address. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Please provide an IP address." if the ipAddress parameter is empty. 

* SoftLayer_Exception_Public 

> Throw the exception "Please provide a PTR address." if the ptrRecord parameter is empty. 

* SoftLayer_Exception_Public 

> Throw the exception "Please provide a valid IP address." if the ipAddress parameter is not a valid IPv4 or IPv6 address. 

* SoftLayer_Exception_Public 

> Throw the exception "Please provide a TTL value between 60 and 604800." if the ttl parameter is less than 60 (one minute) or greater than 604800 (one week). 

* SoftLayer_Exception_Public 

> Throw the exception "Access denied." if the user making the method call does not have access to the IP address they wish to set a PTR record for. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to save PTR record." if the SoftLayer is unable to set your PTR record. 



