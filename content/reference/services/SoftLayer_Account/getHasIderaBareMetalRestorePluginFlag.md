---
title: "getHasIderaBareMetalRestorePluginFlag"
description: "Return 1 if one of the account's hardware has an installation of Idera Server Backup otherwise 0."
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

# [REST Example](#getHasIderaBareMetalRestorePluginFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHasIderaBareMetalRestorePluginFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getHasIderaBareMetalRestorePluginFlag'
```
