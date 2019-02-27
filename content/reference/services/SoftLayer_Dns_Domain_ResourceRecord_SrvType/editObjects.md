---
title: "editObjects"
description: "Edit multiple SRV records on a domain. This follows the same logic as ''createObject'. The serial number of the domain a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_srvtype/editObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord_SrvType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType)::editObjects

Edit multiple domain SRV records.


## Overview 
Edit multiple SRV records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this SRV record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of skeleton SoftLayer_Dns_Domain_ResourceRecord_SrvType objects with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Dns_Domain_ResourceRecord::editObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::editObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_SrvType::editObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType/editObject )




