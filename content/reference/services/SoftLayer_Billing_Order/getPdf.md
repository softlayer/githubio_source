---
title: "getPdf"
description: "Retrieve a PDF record of a SoftLayer quote. If the order is not a quote, an error will be thrown. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order"
---

### [REST Example](#getPdf-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPdf-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getPdf'
```
