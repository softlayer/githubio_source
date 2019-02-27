---
title: "getObject"
description: "getObject retrieves the SoftLayer_Auxiliary_Press_Release object whose ID number corresponds to the ID number of the ini... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release"
aliases:
    - "/reference/services/softlayer_auxiliary_press_release/getObject"
---
# [SoftLayer_Auxiliary_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release)::getObject

Retrieve a SoftLayer_Auxiliary_Press_Release record.


## Overview 
getObject retrieves the SoftLayer_Auxiliary_Press_Release object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Auxiliary_Press_Release service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Auxiliary_Press_ReleaseInitParameters
* authenticate


### Optional Headers
* SoftLayer_Auxiliary_Press_ReleaseObjectMask
* SoftLayer_Auxiliary_Press_ReleaseObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release'>SoftLayer_Auxiliary_Press_Release </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



