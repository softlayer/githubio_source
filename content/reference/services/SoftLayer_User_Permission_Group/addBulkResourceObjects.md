---
title: "addBulkResourceObjects"
description: "Links multiple SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost objects to the group. All objects must be of the same type. "
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

### [REST Example](#addBulkResourceObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addBulkResourceObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Entity, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Group/{SoftLayer_User_Permission_GroupID}/addBulkResourceObjects'
```
