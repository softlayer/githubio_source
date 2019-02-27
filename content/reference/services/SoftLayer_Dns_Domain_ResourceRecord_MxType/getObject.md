---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord_MxType object whose ID number corresponds to the ID number o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_mxtype/getObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord_MxType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType)::getObject

Retrieve a SoftLayer_Dns_Domain_ResourceRecord_MxType record.


## Overview 
getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord_MxType object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain_ResourceRecord_MxType service. You can only retrieve resource records belonging to domains that are assigned to your SoftLayer account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeInitParameters
* authenticate


### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeObjectMask
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType'>SoftLayer_Dns_Domain_ResourceRecord_MxType </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



