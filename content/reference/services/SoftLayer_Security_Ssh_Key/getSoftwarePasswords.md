---
title: "getSoftwarePasswords"
description: "Retrieve the OS root users that are linked to an SSH key."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Ssh_Key"
---
# [SoftLayer_Security_Ssh_Key](/reference/services/SoftLayer_Security_Ssh_Key)::getSoftwarePasswords

Retrieve the OS root users that are linked to an SSH key.


## Overview 
Retrieve the OS root users that are linked to an SSH key.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Security_Ssh_KeyInitParameters
* authenticate

### Optional Headers
* SoftLayer_Security_Ssh_KeyObjectMask
* SoftLayer_Security_Ssh_KeyObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password[] </a>

