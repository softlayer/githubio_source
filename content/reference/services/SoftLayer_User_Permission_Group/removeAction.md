---
title: "removeAction"
description: "Unassigns a SoftLayer_User_Permission_Action object from the group. "
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

### [REST Example](#removeAction-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAction-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Permission_Action]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Group/{SoftLayer_User_Permission_GroupID}/removeAction'
```
