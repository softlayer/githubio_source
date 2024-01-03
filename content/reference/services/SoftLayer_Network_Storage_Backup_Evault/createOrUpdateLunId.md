---
title: "createOrUpdateLunId"
description: "The LUN ID only takes effect during the Host Authorization process. It is required to de-authorize all hosts before using this method. "
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

# [REST Example](#createOrUpdateLunId-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createOrUpdateLunId-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/createOrUpdateLunId'
```
