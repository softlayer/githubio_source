---
title: "getCancellationCutoffDate"
description: "Services can be canceled 2 or 3 days prior to your next bill date. This service returns the time by which a cancellation request submission is permitted in the current billing cycle. If the current time falls into the cut off date, this will return next earliest cancellation cut off date. 

Available category codes are: service, server "
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

# [REST Example](#getCancellationCutoffDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCancellationCutoffDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/getCancellationCutoffDate'
```
