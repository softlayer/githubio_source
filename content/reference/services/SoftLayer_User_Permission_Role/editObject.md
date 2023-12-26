---
title: "editObject"
description: "Allows a user to modify the name and description of an existing customer permission role. Customer permission roles must set the systemFlag attribute to false.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission role must match account id of the user who is creating the permission role.  The user who is creating the permission role must have the permission to manage users. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Permission_Role]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Permission_Role/{SoftLayer_User_Permission_RoleID}/editObject'
```
