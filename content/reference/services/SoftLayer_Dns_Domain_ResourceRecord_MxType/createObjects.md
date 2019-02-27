---
title: "createObjects"
description: "Create multiple MX records on a domain. This follows the same logic as ''createObject'. The serial number of the domain... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_mxtype/createObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord_MxType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType)::createObjects

Create multiple MX records.


## Overview 
Create multiple MX records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this MX record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of SoftLayer_Dns_Domain_ResourceRecord objects that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>


### Associated Methods

*  [SoftLayer_Dns_Domain_ResourceRecord::createObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::createObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_MxType::createObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType/createObject )




