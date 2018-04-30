---
title: "getMonitoringUserNotification"
description: "Retrieve the monitoring notification objects for this hardware. Each object links this hardware instance to a user accou... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getMonitoringUserNotification"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getMonitoringUserNotification

Retrieve the monitoring notification objects for this hardware. Each object links this hardware instance to a user account that will be notified if monitoring on this hardware object fails


## Overview 
Retrieve the monitoring notification objects for this hardware. Each object links this hardware instance to a user account that will be notified if monitoring on this hardware object fails

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_SecurityModuleInitParameters
* authenticate

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_Hardware_SecurityModuleObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a>

