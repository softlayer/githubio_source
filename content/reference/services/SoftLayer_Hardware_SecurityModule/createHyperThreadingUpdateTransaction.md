---
title: "createHyperThreadingUpdateTransaction"
description: "You can launch hyper-threading update by selecting from your server list. It will bring your server offline for approxim... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/createHyperThreadingUpdateTransaction"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::createHyperThreadingUpdateTransaction


Runs BIOS update on the server to change the hyper-threading configuration.


## Overview 
You can launch hyper-threading update by selecting from your server list. It will bring your server offline for approximately 60 minutes while the update is in progress. 

In the event of a hardware failure during this our datacenter engineers will be notified of the problem automatically. They will then replace any failed components to bring your server back online, and will be contacting you to ensure that impact on your server is minimal. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|disableHyperthreading| integer| disable hyper-threading|


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



