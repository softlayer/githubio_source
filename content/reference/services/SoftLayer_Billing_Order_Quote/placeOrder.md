---
title: "placeOrder"
description: "Use this method for placing server orders and additional services orders. The same applies for this as with verifyOrder. Send in the SoftLayer_Container_Product_Order_Hardware_Server for server orders. In addition to verifying the order, placeOrder() also makes an initial authorization on the SoftLayer_Account tied to this order, if a credit card is on file. If the account tied to this order is a paypal customer, an URL will also be returned to the customer. After placing the order, you must go to this URL to finish the authorization process. This tells paypal that you indeed want to place the order. After going to this URL, it will direct you back to a SoftLayer webpage that tells us you have finished the process. After this, it will go to sales for final approval. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Quote"
---

### [REST Example](#placeOrder-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#placeOrder-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/{SoftLayer_Billing_Order_QuoteID}/placeOrder'
```
