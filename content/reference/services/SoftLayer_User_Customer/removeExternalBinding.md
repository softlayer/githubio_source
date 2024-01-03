---
title: "removeExternalBinding"
description: "Remove an external binding from this user."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

# [REST Example](#removeExternalBinding-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeExternalBinding-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_External_Binding]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/removeExternalBinding'
```
