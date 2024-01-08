---
title: "upgradeVolumeCapacity"
description: "Upgrade the Storage volume to one of the upgradable packages (for example from 10 Gigs of EVault storage to 100 Gigs of EVault storage). "
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

### [REST Example](#upgradeVolumeCapacity-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#upgradeVolumeCapacity-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/upgradeVolumeCapacity'
```
