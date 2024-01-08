---
title: "linkExternalAccount"
description: "This method will link this SoftLayer account with the provided external account. "
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

### [REST Example](#linkExternalAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#linkExternalAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/linkExternalAccount'
```
