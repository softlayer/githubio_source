---
title: "getSshKeys"
description: "Retrieve sSH keys to be installed on the server during provisioning or an OS reload."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
aliases:
    - "/reference/services/softlayer_software_component_password/getSshKeys"
---
# [SoftLayer_Software_Component_Password](/reference/services/SoftLayer_Software_Component_Password)::getSshKeys

Retrieve sSH keys to be installed on the server during provisioning or an OS reload.


## Overview 
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.

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
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>




