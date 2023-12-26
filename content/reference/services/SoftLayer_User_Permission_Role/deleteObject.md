---
title: "deleteObject"
description: "Customer users can only delete permission roles with systemFlag set to false.  The SYSTEM type is reserved for internal use. The user who is creating the permission role must have the permission to manage users. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Role/{SoftLayer_User_Permission_RoleID}/deleteObject'
```
