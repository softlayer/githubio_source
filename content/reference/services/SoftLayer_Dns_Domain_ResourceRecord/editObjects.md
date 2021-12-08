---
title: "editObjects"
description: "Edit multiple resource records on a domain. This follows the same logic as ''createObject'. The serial number of the dom... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord/editObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord)::editObjects


Edit multiple domain resource records.


## Overview 
Edit multiple resource records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this resource record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of skeleton SoftLayer_Dns_Domain_ResourceRecord objects with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Dns_ResourceRecord::editObject](/reference/services/SoftLayer_Dns_ResourceRecord/editObject )




