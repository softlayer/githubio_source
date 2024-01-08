---
title: "deleteObject"
description: "Delete a network storage schedule. '''This cannot be undone.''' ''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a schedule; "
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

### [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Schedule/{SoftLayer_Network_Storage_ScheduleID}/deleteObject'
```
