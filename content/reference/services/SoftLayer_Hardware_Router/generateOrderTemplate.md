---
title: "generateOrderTemplate"
description: "
Obtain an [SoftLayer_Container_Product_Order_Hardware_Server](/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server) that can be sent to [SoftLayer_Product_Order::verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder) or [SoftLayer_Product_Order::placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder). 


This is primarily useful when there is a necessity to confirm the price which will be charged for an order. 


See [SoftLayer_Hardware::createObject](/reference/services/SoftLayer_Hardware/createObject) for specifics on the requirements of the template object parameter. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

# [REST Example](#generateOrderTemplate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#generateOrderTemplate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/generateOrderTemplate'
```
