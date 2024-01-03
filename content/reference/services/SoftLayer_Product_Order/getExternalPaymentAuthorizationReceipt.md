---
title: "getExternalPaymentAuthorizationReceipt"
description: "This method simply returns a receipt for a previously finalized payment authorization from PayPal. The response matches the response returned from placeOrder when the order was originally placed with PayPal as the payment type. "
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

# [REST Example](#getExternalPaymentAuthorizationReceipt-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getExternalPaymentAuthorizationReceipt-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/getExternalPaymentAuthorizationReceipt'
```
