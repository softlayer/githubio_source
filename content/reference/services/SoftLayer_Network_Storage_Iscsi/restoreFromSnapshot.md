---
title: "restoreFromSnapshot"
description: "Restore the volume from a snapshot that was previously taken. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Iscsi"
---

### [REST Example](#restoreFromSnapshot-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#restoreFromSnapshot-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/restoreFromSnapshot'
```
