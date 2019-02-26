---
title: "getObject"
description: "getObject retrieves the SoftLayer_Hardware_Server object whose ID number corresponds to the ID number of the init parame... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getObject"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getObject

Retrieve a SoftLayer_Hardware_Server record.


## Overview 
getObject retrieves the SoftLayer_Hardware_Server object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Hardware service. You can only retrieve servers from the account that your portal user is assigned to. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_ServerInitParameters
* authenticate


### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_Hardware_ServerObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 

* SoftLayer_Exception 

> Throw the error "Method has not been implemented for this object type." id the method is used. 

* SoftLayer_Exception_Public 

> Throws the exception 'No operating system could be found for this server.' Then the setOperatingSystemPassword method is called to change the password for a server that does not have an operating system setup. 



