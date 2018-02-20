---
title: "resetStatus"
description: "If our monitoring management system is not able to connect to your monitoring robot, it sets the robot status to 'Limite... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Robot"
---
# SoftLayer_Monitoring_Robot::resetStatus
## Overview 
If our monitoring management system is not able to connect to your monitoring robot, it sets the robot status to "Limited Connectivity". Robots in this status will not be process by our monitoring management system. You cannot manage monitoring agents either. 

Use this method to resets monitoring robot status to "Active" to indicate the connection issue is resolved. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Monitoring_RobotInitParameters

### Optional Headers

### Return Values
boolean
