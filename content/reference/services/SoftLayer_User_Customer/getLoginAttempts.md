---
title: "getLoginAttempts"
description: "A user's attempts to log into the SoftLayer customer portal."
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

# [REST Example](#getLoginAttempts-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLoginAttempts-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getLoginAttempts'
```
