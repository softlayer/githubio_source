---
title: "getObject"
description: "getObject retrieves a SoftLayer_Product_Upgrade_Request object on your account whose ID corresponds to the ID of the ini... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
aliases:
    - "/reference/services/softlayer_product_upgrade_request/getObject"
---
# [SoftLayer_Product_Upgrade_Request](/reference/services/SoftLayer_Product_Upgrade_Request)::getObject

Retrieve a SoftLayer_Product_Upgrade_Request record.


## Overview 
getObject retrieves a SoftLayer_Product_Upgrade_Request object on your account whose ID corresponds to the ID of the init parameter passed to the SoftLayer_Product_Upgrade_Request service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Product_Upgrade_RequestInitParameters
* authenticate


### Optional Headers
* SoftLayer_Product_Upgrade_RequestObjectMask
* SoftLayer_Product_Upgrade_RequestObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



