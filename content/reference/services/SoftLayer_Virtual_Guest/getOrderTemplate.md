---
title: "getOrderTemplate"
description: "Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method. This container will include all services that the selected computing instance has. If desired you may remove prices which were returned. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [enum, SoftLayer_Product_Item_Price]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getOrderTemplate'
```
