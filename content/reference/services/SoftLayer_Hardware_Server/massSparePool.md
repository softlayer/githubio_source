---
title: "massSparePool"
description: "The ability to place multiple bare metal servers in a state where they are powered down and ports closed yet still alloc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/massSparePool"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::massSparePool


Allows multiple servers to be added to or removed from the spare pool.


## Overview 
The ability to place multiple bare metal servers in a state where they are powered down and ports closed yet still allocated to the customer as a part of the Spare Pool program. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareIds| array of strings| List of hardware ids to be added/removed from spare pool|
|action| string| Action to 'add' server to spare pool or remove (use 'activate') from spare pool|
|newOrder| boolean| Set to true if a Spare Pool Server was ordered; otherwise false|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Request'>SoftLayer_Container_Hardware_Server_Request[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Issue OS Reloads. 

* SoftLayer_Exception_Public 

> Throws the exception 'There is currently an outstanding transaction for this server.' when there is a current hardware update. 



