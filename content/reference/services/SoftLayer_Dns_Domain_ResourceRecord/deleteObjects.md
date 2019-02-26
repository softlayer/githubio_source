---
title: "deleteObjects"
description: "Remove multiple resource records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord/deleteObjects"
---
# [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord)::deleteObjects

Delete multiple resource records from a domain.


## Overview 
Remove multiple resource records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. The serial number of the domain associated with this resource record is updated upon deletion. You may not delete SOA records, PTR records, or NS resource records that point to ns1.softlayer.com or ns2.softlayer.com. 

''deleteObjects'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of skeleton SoftLayer_Dns_Domain_ResourceRecord objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Dns_ResourceRecord::deleteObject](/reference/services/SoftLayer_Dns_ResourceRecord/deleteObject )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "SOA records may not be removed." when attempting to remove an SOA resource record. 

* SoftLayer_Exception 

> Throw the exception "NS records for ns1.softlayer.com or ns2.softlayer.com may not be removed." when attempting to remove an NS resource record that points to ns1.softlayer.com or ns2.softlayer.com. 

* SoftLayer_Exception 

> Throw the exception "PTR records may not be removed." when attempting to remove a PTR resource record. 



