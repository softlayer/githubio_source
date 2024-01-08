---
title: "getAllCancellationRequests"
description: "This method returns all service cancellation requests. 

Make sure to include the 'resultLimit' in the SOAP request header for quicker response. If there is no result limit header is passed, it will return the latest 25 results by default. "
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

### [REST Example](#getAllCancellationRequests-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllCancellationRequests-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/getAllCancellationRequests'
```
