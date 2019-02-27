---
title: "deleteObject"
description: "Delete a domain's resource record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord/deleteObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord)::deleteObject

Delete a domain's resource record.


## Overview 
Delete a domain's resource record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource record in error you will need to re-create it by creating a new SoftLayer_Dns_Domain_ResourceRecord object. The serial number of the domain associated with this resource record is updated upon deletion. You may not delete SOA, NS, or PTR resource records. 

''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_ResourceRecordInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Dns_ResourceRecord::deleteObjects](/reference/services/SoftLayer_Dns_ResourceRecord/deleteObjects )



### Error Handling

* SoftLayer_Exception 

> Throw the exception "SOA records may not be removed." when attempting to remove an SOA resource record. 

* SoftLayer_Exception 

> Throw the exception "NS records may not be removed." when attempting to remove an NS resource record. 

* SoftLayer_Exception 

> Throw the exception "PTR records may not be removed." when attempting to remove a PTR resource record. 



