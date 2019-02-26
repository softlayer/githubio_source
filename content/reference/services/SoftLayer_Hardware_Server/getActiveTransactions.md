---
title: "getActiveTransactions"
description: "Retrieve any active transaction(s) that are currently running for the server (example: os reload)."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getActiveTransactions"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getActiveTransactions

Retrieve any active transaction(s) that are currently running for the server (example: os reload).


## Overview 
Retrieve any active transaction(s) that are currently running for the server (example: os reload).

-----

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
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>




