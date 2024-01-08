---
title: "migrateExternalAccount"
description: "Will attempt to migrate an external account to the brand in context. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand"
---

### [REST Example](#migrateExternalAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#migrateExternalAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/{SoftLayer_BrandID}/migrateExternalAccount'
```
