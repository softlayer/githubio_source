---
title: "getVdrUpdatesInProgressFlag"
description: "DEPRECATED - Return 0 if VDR updates are currently in progress on this account otherwise 1."
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

### [REST Example](#getVdrUpdatesInProgressFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVdrUpdatesInProgressFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getVdrUpdatesInProgressFlag'
```
