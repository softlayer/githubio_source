---
title: "editObject"
description: "Edit a nas volume schedule "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Schedule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Schedule"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage_Schedule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Schedule/{SoftLayer_Network_Storage_ScheduleID}/editObject'
```
