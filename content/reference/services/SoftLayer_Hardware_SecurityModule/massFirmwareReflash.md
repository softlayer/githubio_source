---
title: "massFirmwareReflash"
description: "You can launch firmware reflashes by selecting from your server list. It will bring your server offline for approximatel... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/massFirmwareReflash"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::massFirmwareReflash

Runs firmware reflashes on the servers components.


## Overview 
You can launch firmware reflashes by selecting from your server list. It will bring your server offline for approximately 60 minutes while the reflashes are in progress. 

In the event of a hardware failure during this test our datacenter engineers will be notified of the problem automatically. They will then replace any failed components to bring your server back online. They will be contact you to ensure that impact on your server is minimal. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareIds| array of integers| List of hardware ids to have firmware reflashed.|
|ipmi| boolean| Flag to determine whether IPMI firmware reflash should occur.|
|raidController| boolean| Flag to determine whether raid controller firmware reflash should occur.|
|bios| boolean| Flag to determine whether BIOS firmware reflash should occur.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Request'>SoftLayer_Container_Hardware_Server_Request[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Issue OS Reloads. 



