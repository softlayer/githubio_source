---
title: "initiateIderaBareMetalRestore"
description: "Idera Bare Metal Server Restore is a backup agent designed specifically for making full system restores made with Idera... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/initiateIderaBareMetalRestore"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::initiateIderaBareMetalRestore

Initiate an Idera bare metal restore for the server tied to an Idera Server Backup


## Overview 
Idera Bare Metal Server Restore is a backup agent designed specifically for making full system restores made with Idera Server Backup. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Issue OS Reloads. 

* SoftLayer_Exception_Public 

> Throws the exception 'There is currently an outstanding transaction for this server.' when there is a current hardware update. 



