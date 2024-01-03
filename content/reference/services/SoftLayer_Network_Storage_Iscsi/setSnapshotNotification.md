---
title: "setSnapshotNotification"
description: "Function to enable/disable snapshot warning notification. "
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

# [REST Example](#setSnapshotNotification-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setSnapshotNotification-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/setSnapshotNotification'
```
