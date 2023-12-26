---
title: "editObjects"
description: "Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other user's information. Use editObjects() if you wish to edit multiple users at once. Users who do not have the User Manage permission can only update their own information. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/editObjects'
```
