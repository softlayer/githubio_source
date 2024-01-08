---
title: "createOpenIdConnectUserAndCompleteInvitation"
description: "Completes invitation processing when a new OpenIdConnect user must be created."
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

### [REST Example](#createOpenIdConnectUserAndCompleteInvitation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createOpenIdConnectUserAndCompleteInvitation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_User_Customer, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/createOpenIdConnectUserAndCompleteInvitation'
```
