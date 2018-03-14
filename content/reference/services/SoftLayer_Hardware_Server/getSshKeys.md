---
title: "getSshKeys"
description: "Retrieve sSH keys to be installed on the server during provisioning or an OS reload."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getSshKeys"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getSshKeys

Retrieve sSH keys to be installed on the server during provisioning or an OS reload.


## Overview 
Retrieve sSH keys to be installed on the server during provisioning or an OS reload.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_ServerInitParameters
* authenticate

### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_Hardware_ServerObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>

