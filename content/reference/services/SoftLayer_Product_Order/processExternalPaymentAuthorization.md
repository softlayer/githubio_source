---
title: "processExternalPaymentAuthorization"
description: "This method simply finalizes an authorization from PayPal. It tells SoftLayer that the customer has completed the PayPal process. This is ONLY needed if you, the customer, have your own API into PayPal and wish to automate authorizations from PayPal and our system. For most, this method will not be needed. Once an order is placed using placeOrder() for PayPal customers, a URL is given back to the customer. In it is the token and PayerID. If you want to systematically pay with PayPal, do so then call this method with the token and PayerID. "
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

# [REST Example](#processExternalPaymentAuthorization-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#processExternalPaymentAuthorization-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/processExternalPaymentAuthorization'
```
