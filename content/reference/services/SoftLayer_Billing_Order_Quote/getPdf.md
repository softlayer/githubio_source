---
title: "getPdf"
description: "Retrieve a PDF record of a SoftLayer quoted order. SoftLayer keeps PDF records of all quoted orders for customer retrieval from the portal and API. You must have a PDF reader installed in order to view these quoted order files. "
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

# [REST Example](#getPdf-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPdf-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/{SoftLayer_Billing_Order_QuoteID}/getPdf'
```
