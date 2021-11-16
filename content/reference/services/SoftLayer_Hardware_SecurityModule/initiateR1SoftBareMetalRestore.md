---
title: "initiateR1SoftBareMetalRestore"
description: "R1Soft Bare Metal Server Restore is an R1Soft disk agent designed specifically for making full system restores made with... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/initiateR1SoftBareMetalRestore"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::initiateR1SoftBareMetalRestore


Initiate an R1Soft bare metal restore for the server tied to an R1Soft CDP Server


## Overview 
R1Soft Bare Metal Server Restore is an R1Soft disk agent designed specifically for making full system restores made with R1Soft CDP Server backup. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Issue OS Reloads. 

* SoftLayer_Exception_Public 

> Throws the exception 'There is currently an outstanding transaction for this server.' when there is a current hardware update. 



