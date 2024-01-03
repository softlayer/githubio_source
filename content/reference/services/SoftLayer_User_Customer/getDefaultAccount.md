---
title: "getDefaultAccount"
description: "This method is not applicable to legacy SoftLayer-authenticated users and can only be invoked for IBMid-authenticated users. "
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

# [REST Example](#getDefaultAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDefaultAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getDefaultAccount'
```
