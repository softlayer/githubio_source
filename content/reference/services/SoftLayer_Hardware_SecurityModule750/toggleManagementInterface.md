---
title: "toggleManagementInterface"
description: "Attempt to toggle the IPMI interface.  If there is an active transaction on the server, it will throw an exception. This... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/toggleManagementInterface"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::toggleManagementInterface

Toggle the IPMI interface on and off.


## Overview 
Attempt to toggle the IPMI interface.  If there is an active transaction on the server, it will throw an exception. This method creates a transaction to toggle the interface.  It is not instant. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|enabled| boolean| Whether to enable or disable the interface.|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* boolean




