---
title: "getResellerOrder"
description: "When the account is on an external reseller brand, this service will provide a SoftLayer_Product_Order with the the pricing adjusted by the external reseller. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/getResellerOrder'
```
