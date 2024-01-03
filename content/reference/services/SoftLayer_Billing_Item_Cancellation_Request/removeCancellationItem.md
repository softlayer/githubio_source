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

# [REST Example](#removeCancellationItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeCancellationItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/{SoftLayer_Billing_Item_Cancellation_RequestID}/removeCancellationItem'
```
