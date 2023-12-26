---
title: "enableSnapshots"
description: "This method is not valid for Legacy iSCSI Storage Volumes. 

Enable scheduled snapshots of this storage volume. Scheduling options include HOURLY, DAILY and WEEKLY schedules. For HOURLY schedules, provide relevant data for $scheduleType, $retentionCount and $minute. For DAILY schedules, provide relevant data for $scheduleType, $retentionCount, $minute, and $hour. For WEEKLY schedules, provide relevant data for all parameters of this method. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Backup_Evault"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/enableSnapshots'
```
