---
title: "createObject"
description: "Customer created permission groups must be of type NORMAL.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission group must match account id of the user who is creating the permission group.  The user who is creating the permission group must have the permission to manage users. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Permission_Group]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Group/createObject'
```
