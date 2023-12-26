---
title: "getQuoteByQuoteKey"
description: "This method will return a [SoftLayer_Billing_Order_Quote](/reference/datatypes/SoftLayer_Billing_Order_Quote) that is identified by the quote key specified. If you do not have access to the quote or it does not exist, an exception will be thrown indicating so. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Cart/getQuoteByQuoteKey'
```
