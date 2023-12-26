---
title: "deleteObject"
description: "Delete a network storage volume. '''This cannot be undone.''' At this time only network storage snapshots may be deleted with this method. 

''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a volume; "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/deleteObject'
```
