---
title: "checkConnection"
description: "Checks if a monitoring robot can communicate with SoftLayer monitoring management system via the private network. 

TCP... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Robot"
---
# SoftLayer_Monitoring_Robot::checkConnection
## Overview 
Checks if a monitoring robot can communicate with SoftLayer monitoring management system via the private network. 

TCP port 48000 - 48002 must be open on your server or your virtual server in order for this test to succeed. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Monitoring_RobotInitParameters

### Optional Headers

### Return Values
boolean
