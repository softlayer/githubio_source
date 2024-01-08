---
title: "getManualSnapshots"
description: "The manually-created snapshots associated with this SoftLayer_Network_Storage volume. Does not support pagination by result limit and offset."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

### [REST Example](#getManualSnapshots-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getManualSnapshots-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getManualSnapshots'
```
