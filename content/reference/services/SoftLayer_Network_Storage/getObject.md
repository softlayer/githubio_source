---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Storage object whose ID corresponds to the ID number of the init parameter pas... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/getObject"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getObject

Retrieve a SoftLayer_Network_Storage record.


## Overview 
getObject retrieves the SoftLayer_Network_Storage object whose ID corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Storage service. 

Please use the associated methods in the [SoftLayer_Network_Storage]({{<ref "reference/datatypes/SoftLayer_Network_Storage">}}) service to retrieve a Storage account's id. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_StorageInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_StorageObjectMask
* SoftLayer_Network_StorageObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



