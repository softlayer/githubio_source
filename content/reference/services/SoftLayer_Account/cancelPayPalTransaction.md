---
title: "cancelPayPalTransaction"
description: "(DEPRECATED) Cancel the PayPal Payment Request process."
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

### [REST Example](#cancelPayPalTransaction-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#cancelPayPalTransaction-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/cancelPayPalTransaction'
```
