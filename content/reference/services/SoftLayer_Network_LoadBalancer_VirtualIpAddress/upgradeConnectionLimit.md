---
title: "upgradeConnectionLimit"
description: "Upgrades the connection limit on the VirtualIp and changes the billing item on your account to reflect the change. This... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---
# SoftLayer_Network_LoadBalancer_VirtualIpAddress::upgradeConnectionLimit
## Overview 
Upgrades the connection limit on the VirtualIp and changes the billing item on your account to reflect the change. This function will only upgrade you to the next "level" of service.  The next level follows this pattern Current Level  =>  Next Level 50                 100 100                200 200                500 500                1000 1000               1200 1200               1500 1500               2000 2000               2500 2500               3000 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_VirtualIpAddressInitParameters

### Optional Headers

### Return Values
boolean
