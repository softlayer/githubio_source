---
title: "getTicket"
description: "The ticket that is associated with the service cancellation request."
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

### [REST Example](#getTicket-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTicket-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/{SoftLayer_Billing_Item_Cancellation_RequestID}/getTicket'
```
