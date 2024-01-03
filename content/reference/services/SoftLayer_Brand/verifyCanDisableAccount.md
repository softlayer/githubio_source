---
title: "verifyCanDisableAccount"
description: "Verify that an account may be disabled by a Brand Agent.  Anything that would disqualify the account from being disabled will cause an exception to be raised. "
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

# [REST Example](#verifyCanDisableAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#verifyCanDisableAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/{SoftLayer_BrandID}/verifyCanDisableAccount'
```
