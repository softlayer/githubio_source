---
title: "createFirmwareReflashTransaction"
description: "You can launch firmware reflash by selecting from your server list. It will bring your server offline for approximately... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/createFirmwareReflashTransaction"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::createFirmwareReflashTransaction


Runs firmware reflash on the servers components.


## Overview 
You can launch firmware reflash by selecting from your server list. It will bring your server offline for approximately 60 minutes while the flashes are in progress. 

In the event of a hardware failure during this our datacenter engineers will be notified of the problem automatically. They will then replace any failed components to bring your server back online, and will be contacting you to ensure that impact on your server is minimal. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipmi| integer| reflash ipmi firmware|
|raidController| integer| reflash raid controller firmware|
|bios| integer| reflash bios firmware|


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



