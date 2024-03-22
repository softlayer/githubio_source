---
title: "getBlockSelfServiceBrandMigration"
description: "Flag indicating whether this account is restricted from performing a self-service brand migration by updating their credit card details."
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

### [REST Example](#getBlockSelfServiceBrandMigration-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBlockSelfServiceBrandMigration-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getBlockSelfServiceBrandMigration'
```
