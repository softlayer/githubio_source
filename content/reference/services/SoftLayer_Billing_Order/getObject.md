---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Order object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Order service. You can only retrieve orders that are assigned to your portal user's account. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getObject'
```
