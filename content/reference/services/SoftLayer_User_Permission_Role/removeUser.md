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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Role/{SoftLayer_User_Permission_RoleID}/removeUser'
```
