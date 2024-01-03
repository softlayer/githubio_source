---
title: "getApiAuthenticationKeys"
description: "A portal user's API Authentication keys. There is a max limit of one API key per user."
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

# [REST Example](#getApiAuthenticationKeys-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getApiAuthenticationKeys-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getApiAuthenticationKeys'
```
