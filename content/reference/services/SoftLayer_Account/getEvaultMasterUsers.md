---
title: "getEvaultMasterUsers"
description: "An account's master EVault user. This is only used when an account has EVault service."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

# [REST Example](#getEvaultMasterUsers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getEvaultMasterUsers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getEvaultMasterUsers'
```
