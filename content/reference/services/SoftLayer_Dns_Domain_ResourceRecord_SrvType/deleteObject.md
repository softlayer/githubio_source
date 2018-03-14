---
title: "deleteObject"
description: "Delete a domain's SRV record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource reco... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_srvtype/deleteObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord_SrvType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType)::deleteObject

Delete a domain's SRV record.


## Overview 
Delete a domain's SRV record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource record in error you will need to re-create it by creating a new SoftLayer_Dns_Domain_ResourceRecord_SrvType object. The serial number of the domain associated with this SRV record is updated upon deletion. 

''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_ResourceRecord_SrvTypeInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::deleteObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_SrvType::deleteObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType/deleteObjects )

