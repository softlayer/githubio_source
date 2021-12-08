---
title: "getObject"
description: "getObject retrieves the SoftLayer_Account object whose ID number corresponds to the ID number of the init parameter pass... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getObject"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getObject


Retrieve a SoftLayer_Account record.


## Overview 
getObject retrieves the SoftLayer_Account object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Account service. You can only retrieve the account that your portal user is assigned to. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_AccountObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> <<< EOT 

* SoftLayer_Exception_AccessDenied 

> <<< EOT 



