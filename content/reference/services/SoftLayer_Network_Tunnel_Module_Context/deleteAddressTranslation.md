---
title: "deleteAddressTranslation"
description: "Remove an existing address translation from a network tunnel. 

Address translations deliver packets to a destination ip... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::deleteAddressTranslation
## Overview 
Remove an existing address translation from a network tunnel. 

Address translations deliver packets to a destination ip address that is on a customer subnet (remote). 

NOTE:  A network tunnel's configurations must be applied to the network device in order for an address translation to be deleted. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|translationId| integer| The internal identifier for an address translation that needs to be removed for an IPSec network tunnel.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
