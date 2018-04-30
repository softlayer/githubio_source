---
title: "createObjects"
description: "Create multiple resource records on a domain. This follows the same logic as ''createObject'. The serial number of the d... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord/createObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord)::createObjects

Create multiple domain resource records.


## Overview 
Create multiple resource records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this resource record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of SoftLayer_Dns_Domain_ResourceRecord objects that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecordObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::createObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject )

