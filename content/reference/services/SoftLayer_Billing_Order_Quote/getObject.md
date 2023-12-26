---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Order_Quote object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Order_Quote service. You can only retrieve quotes that are assigned to your portal user's account. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/{SoftLayer_Billing_Order_QuoteID}/getObject'
```
