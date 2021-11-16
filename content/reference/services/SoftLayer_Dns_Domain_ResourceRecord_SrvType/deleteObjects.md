---
title: "deleteObjects"
description: "Remove multiple SRV records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. T... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_srvtype/deleteObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord_SrvType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType)::deleteObjects


Delete multiple SRV records from a domain.


## Overview 
Remove multiple SRV records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. The serial number of the domain associated with this SRV record is updated upon deletion. 

''deleteObjects'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of skeleton SoftLayer_Dns_Domain_ResourceRecord_SrvType objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_SrvType::deleteObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType/deleteObject )




