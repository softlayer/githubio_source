---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord_SrvType object whose ID number corresponds to the ID number... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_srvtype/getObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord_SrvType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType)::getObject


Retrieve a SoftLayer_Dns_Domain_ResourceRecord_SrvType record.


## Overview 
getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord_SrvType object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain_ResourceRecord_SrvType service. You can only retrieve resource records belonging to domains that are assigned to your SoftLayer account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Dns_Domain_ResourceRecord_SrvTypeInitParameters
* authenticate


### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecord_SrvTypeObjectMask
* SoftLayer_Dns_Domain_ResourceRecord_SrvTypeObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SrvType'>SoftLayer_Dns_Domain_ResourceRecord_SrvType </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



