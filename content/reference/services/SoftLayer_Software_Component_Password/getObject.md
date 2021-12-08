---
title: "getObject"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
aliases:
    - "/reference/services/softlayer_software_component_password/getObject"
---
# [SoftLayer_Software_Component_Password](/reference/services/SoftLayer_Software_Component_Password)::getObject


Retrieve a SoftLayer_Software_Component_Password record.


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Software_Component_PasswordInitParameters
* authenticate


### Optional Headers
* SoftLayer_Software_Component_PasswordObjectMask
* SoftLayer_Software_Component_PasswordObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the error "Maximum of 3 passwords per software title." if three passwords are already being stored. 



