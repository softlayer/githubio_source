---
title: "getOrderTotalOneTime"
description: "An order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getOrderTotalOneTime'
```
