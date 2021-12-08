---
title: "getObject"
description: "getObject retrieves the SoftLayer_Hardware object whose ID number corresponds to the ID number of the init parameter pas... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/getObject"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::getObject


Retrieve a SoftLayer_Hardware record.


## Overview 
getObject retrieves the SoftLayer_Hardware object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Hardware service. You can only retrieve the account that your portal user is assigned to. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_HardwareInitParameters
* authenticate


### Optional Headers
* SoftLayer_HardwareObjectMask
* SoftLayer_HardwareObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> <<< EOT 

* SoftLayer_Exception_AccessDenied 

> <<< EOT 

* SoftLayer_Exception 

> <<< EOT 



