---
title: "deleteObjects"
description: "Remove multiple MX records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. Th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_mxtype/deleteObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord_MxType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType)::deleteObjects


Delete multiple MX records from a domain.


## Overview 
Remove multiple MX records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. The serial number of the domain associated with this MX record is updated upon deletion. 

''deleteObjects'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of skeleton SoftLayer_Dns_Domain_ResourceRecord_MxType objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_MxType::deleteObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType/deleteObject )




