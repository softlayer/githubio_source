---
title: "deleteObject"
description: "Delete a domain's MX record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource recor... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_mxtype/deleteObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord_MxType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType)::deleteObject

Delete a domain's MX record.


## Overview 
Delete a domain's MX record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource record in error you will need to re-create it by creating a new SoftLayer_Dns_Domain_ResourceRecord_MxType object. The serial number of the domain associated with this MX record is updated upon deletion. 

''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_MxType::deleteObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType/deleteObjects )

