---
title: "failoverToReplicant"
description: "Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not be available. "
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

### [REST Example](#failoverToReplicant-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#failoverToReplicant-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/failoverToReplicant'
```
