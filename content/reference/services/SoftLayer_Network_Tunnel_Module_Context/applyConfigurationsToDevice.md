---
title: "applyConfigurationsToDevice"
description: "A transaction will be created to apply the IPSec network tunnel's configuration to SoftLayer network devices.  During th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice
## Overview 
A transaction will be created to apply the IPSec network tunnel's configuration to SoftLayer network devices.  During this time, an IPSec network tunnel cannot be modified in anyway.  Only one network tunnel configuration transaction can be created.  If a transaction has been created or is running, a new transaction cannot be created until the previous transaction completes. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
