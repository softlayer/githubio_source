---
title: "deleteObject"
description: "deleteObject permanently removes a domain and all of it's associated resource records from the softlayer name servers. '... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
aliases:
    - "/reference/services/softlayer_dns_domain/deleteObject"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::deleteObject


Remove a domain.


## Overview 
deleteObject permanently removes a domain and all of it's associated resource records from the softlayer name servers. '''This cannot be undone.''' Be wary of running this method. If you remove a domain in error you will need to re-create it by creating a new SoftLayer_Dns_Domain object. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_DomainInitParameters


### Return Values
* boolean




