---
title: "sparePool"
description: "The ability to place bare metal servers in a state where they are powered down, and ports closed yet still allocated to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/sparePool"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::sparePool


Allows servers to be added to or removed from the spare pool.


## Overview 
The ability to place bare metal servers in a state where they are powered down, and ports closed yet still allocated to the customer as a part of the Spare Pool program. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|action| string| Action to 'add' server to spare pool or remove (use 'activate') from spare pool|
|newOrder| boolean| Set to true if a Spare Pool Server was ordered; otherwise false|


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



