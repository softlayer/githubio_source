---
title: "getPrice"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Currency_ExchangeRate"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Currency_ExchangeRate"
---

### [REST Example](#getPrice-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrice-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [float, SoftLayer_Container_Billing_Currency_Format]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Currency_ExchangeRate/{SoftLayer_Billing_Currency_ExchangeRateID}/getPrice'
```
