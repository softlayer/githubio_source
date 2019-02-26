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
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/disableSnapshots"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::disableSnapshots

Disable snapshots of this Storage Volume on a schedule.


## Overview 
This method is not valid for Legacy iSCSI Storage Volumes. 

Disable scheduled snapshots of this storage volume. Scheduling options include 'INTERVAL', HOURLY, DAILY and WEEKLY schedules. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|scheduleType| string| The type of schedule, among: 'INTERVAL', 'HOURLY', 'DAILY', 'WEEKLY'.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* boolean




