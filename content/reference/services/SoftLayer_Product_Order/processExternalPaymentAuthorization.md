---
title: "processExternalPaymentAuthorization"
description: "(DEPRECATED) Process an external (PayPal) payment authorization."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Order"
---

### [REST Example](#processExternalPaymentAuthorization-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#processExternalPaymentAuthorization-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/processExternalPaymentAuthorization'
```
