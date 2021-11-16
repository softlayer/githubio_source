---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord object whose ID number corresponds to the ID number of the i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord/getObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord)::getObject


Retrieve a SoftLayer_Dns_Domain_ResourceRecord record.


## Overview 
getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain_ResourceRecord service. You can only retrieve resource records belonging to domains that are assigned to your SoftLayer account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Dns_Domain_ResourceRecordInitParameters
* authenticate


### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecordObjectMask
* SoftLayer_Dns_Domain_ResourceRecordObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



