---
title: "activateOpenIdConnectUser"
description: "Completes invitation process for an OpenIdConnect user created by Bluemix Unified User Console. "
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

# [REST Example](#activateOpenIdConnectUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#activateOpenIdConnectUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_User_Customer, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/activateOpenIdConnectUser'
```
