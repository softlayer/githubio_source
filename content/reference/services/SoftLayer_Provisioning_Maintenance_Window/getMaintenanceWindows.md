---
title: "getMaintenanceWindows"
description: "This method returns a list of available maintenance windows"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Window"
---
# SoftLayer_Provisioning_Maintenance_Window::getMaintenanceWindows
## Overview 
This method returns a list of available maintenance windows 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|beginDate| dateTime| The beginning date of the date range you wish to search for maintenance windows in.|
|endDate| dateTime| The ending date of the date range you wish to search for maintenance windows in.|
|locationId| integer| The location of the data center that you wish to search for maintenance windows in.|
|slotsNeeded| integer| The number of slots required for the maintenance window.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Provisioning_Maintenance_WindowObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Window'>SoftLayer_Provisioning_Maintenance_Window[] </a>
