---
title: "removeCancellationItem"
description: "This method removes a cancellation item from a cancellation request that is in 'Pending' or 'Approved' status. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Cancellation_Request"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/{SoftLayer_Billing_Item_Cancellation_RequestID}/removeCancellationItem'
```
