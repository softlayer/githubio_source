---
title: "enableSnapshots"
description: "This method is not valid for Legacy iSCSI Storage Volumes. 

Enable scheduled snapshots of this storage volume. Scheduli... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/enableSnapshots"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::enableSnapshots

Enable snapshots of this Storage Volume on a schedule.


## Overview 
This method is not valid for Legacy iSCSI Storage Volumes. 

Enable scheduled snapshots of this storage volume. Scheduling options include HOURLY, DAILY and WEEKLY schedules. For HOURLY schedules, provide relevant data for $scheduleType, $retentionCount and $minute. For DAILY schedules, provide relevant data for $scheduleType, $retentionCount, $minute, and $hour. For WEEKLY schedules, provide relevant data for all parameters of this method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|scheduleType| string| The type of schedule, among: 'INTERVAL', 'HOURLY', 'DAILY', 'WEEKLY'.|
|retentionCount| integer| The number of snapshots to attempt to retain in this schedule.|
|minute| integer| The minute of the hour at which HOURLY, DAILY, and WEEKLY snapshots should be taken.|
|hour| integer| The hour of the day at which DAILY and WEEKLY snapshots should be taken.|
|dayOfWeek| string| The day of the week on which WEEKLY snapshots should be taken, either as a string ('SUNDAY') or integer (cron-notation: '0' is Sunday)|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers

### Return Values
boolean

