---
title: "getIscsiReplicatingVolume"
description: "The network storage volumes configured to be replicants of this volume."
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

### [REST Example](#getIscsiReplicatingVolume-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getIscsiReplicatingVolume-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/getIscsiReplicatingVolume'
```
