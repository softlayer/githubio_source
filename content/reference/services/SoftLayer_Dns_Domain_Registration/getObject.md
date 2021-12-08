---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain_Registration object whose ID number corresponds to the ID number of the ini... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
aliases:
    - "/reference/services/softlayer_dns_domain_registration/getObject"
---
# [SoftLayer_Dns_Domain_Registration](/reference/services/SoftLayer_Dns_Domain_Registration)::getObject


Retrieve a SoftLayer_Dns_Domain_Registration record.


## Overview 
getObject retrieves the SoftLayer_Dns_Domain_Registration object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain_Registration service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Dns_Domain_RegistrationInitParameters
* authenticate


### Optional Headers
* SoftLayer_Dns_Domain_RegistrationObjectMask
* SoftLayer_Dns_Domain_RegistrationObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration'>SoftLayer_Dns_Domain_Registration </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



