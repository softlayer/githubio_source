---
title: "placeQuote"
description: "Use this method for placing server quotes and additional services quotes. The same applies for this as with verifyOrder. Send in the SoftLayer_Container_Product_Order_Hardware_Server for server quotes. After placing the quote, you must go to this URL to finish the order process. After going to this URL, it will direct you back to a SoftLayer webpage that tells us you have finished the process. After this, it will go to sales for final approval. "
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

# [REST Example](#placeQuote-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#placeQuote-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeQuote'
```
