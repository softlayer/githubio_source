---
title: "disableSnapshots"
description: "This method is not valid for Legacy iSCSI Storage Volumes. 

Disable scheduled snapshots of this storage volume. Schedul... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::disableSnapshots
## Overview 
This method is not valid for Legacy iSCSI Storage Volumes. 

Disable scheduled snapshots of this storage volume. Scheduling options include 'INTERVAL', HOURLY, DAILY and WEEKLY schedules. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|scheduleType| string| The type of schedule, among: 'INTERVAL', 'HOURLY', 'DAILY', 'WEEKLY'.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers

### Return Values
boolean
