---
title: "addRole"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
---

### [REST Example](#addRole-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addRole-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Permission_Role]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/addRole'
```
