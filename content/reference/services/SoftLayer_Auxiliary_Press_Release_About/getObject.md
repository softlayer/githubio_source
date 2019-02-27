---
title: "getObject"
description: "getObject retrieves the SoftLayer_Auxiliary_Press_Release_About object whose about id number corresponds to the ID numbe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release_About"
aliases:
    - "/reference/services/softlayer_auxiliary_press_release_about/getObject"
---
# [SoftLayer_Auxiliary_Press_Release_About](/reference/services/SoftLayer_Auxiliary_Press_Release_About)::getObject

Retrieve a SoftLayer_Auxiliary_Press_Release_About record.


## Overview 
getObject retrieves the SoftLayer_Auxiliary_Press_Release_About object whose about id number corresponds to the ID number of the init parameter passed to the SoftLayer_Auxiliary_Press_Release service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Auxiliary_Press_Release_AboutInitParameters
* authenticate


### Optional Headers
* SoftLayer_Auxiliary_Press_Release_AboutObjectMask
* SoftLayer_Auxiliary_Press_Release_AboutObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About'>SoftLayer_Auxiliary_Press_Release_About </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



