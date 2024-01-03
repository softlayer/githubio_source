---
title: "getCartByCartKey"
description: "Retrieve a valid cart record of a SoftLayer order. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Cart"
---

# [REST Example](#getCartByCartKey-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCartByCartKey-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Cart/getCartByCartKey'
```
