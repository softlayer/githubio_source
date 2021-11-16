---
title: "getObject"
description: "getObject retrieves the SoftLayer_Auxiliary_Press_Release_Contact object whose contact id number corresponds to the ID n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release_Media_Partner"
aliases:
    - "/reference/services/softlayer_auxiliary_press_release_media_partner/getObject"
---
# [SoftLayer_Auxiliary_Press_Release_Media_Partner](/reference/services/SoftLayer_Auxiliary_Press_Release_Media_Partner)::getObject


Retrieve a SoftLayer_Auxiliary_Press_Release_Media_Partner record.


## Overview 
getObject retrieves the SoftLayer_Auxiliary_Press_Release_Contact object whose contact id number corresponds to the ID number of the init parameter passed to the SoftLayer_Auxiliary_Press_Release service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Auxiliary_Press_Release_Media_PartnerInitParameters
* authenticate


### Optional Headers
* SoftLayer_Auxiliary_Press_Release_Media_PartnerObjectMask
* SoftLayer_Auxiliary_Press_Release_Media_PartnerObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Media_Partner'>SoftLayer_Auxiliary_Press_Release_Media_Partner </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



