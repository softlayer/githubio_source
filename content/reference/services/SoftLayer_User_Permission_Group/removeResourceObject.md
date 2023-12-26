---
title: "removeResourceObject"
description: "Unlinks a SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost object from the group. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Permission_Group"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Entity, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Group/{SoftLayer_User_Permission_GroupID}/removeResourceObject'
```
