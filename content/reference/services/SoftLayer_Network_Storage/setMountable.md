---
title: "setMountable"
description: "Enable or disable the mounting of a Storage volume. When mounting is enabled the Storage volume will be mountable or ava... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/setMountable"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::setMountable


Enable or disable mounting of a Storage volume.


## Overview 
Enable or disable the mounting of a Storage volume. When mounting is enabled the Storage volume will be mountable or available for use. 

For Virtual Server volumes, disabling mounting will deny access to the Virtual Server Account, remove published material and deny all file interaction including uploads and downloads. 

Enabling or disabling mounting for Storage volumes is not possible if mounting has been disabled by SoftLayer or a parent account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|mountable| boolean| Whether or not the volume should be mountable.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Return Values
* boolean




