---
title: "removeUser"
description: "Unassigns a SoftLayer_User_Customer object from the role. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Permission_Role"
---

# [REST Example](#removeUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Role/{SoftLayer_User_Permission_RoleID}/removeUser'
```
