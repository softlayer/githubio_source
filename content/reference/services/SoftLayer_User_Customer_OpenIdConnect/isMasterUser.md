---
title: "isMasterUser"
description: "Portal users are considered master users if they don't have an associated parent user. The only users who don't have parent users are users whose username matches their SoftLayer account name. Master users have special permissions throughout the SoftLayer customer portal. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/isMasterUser'
```
