---
title: "createObject"
description: "Customer created permission roles must set the systemFlag attribute to false.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission group must match account id of the user who is creating the permission group.  The user who is creating the permission group must have the permission to manage users. "
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

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Permission_Role]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Role/createObject'
```
