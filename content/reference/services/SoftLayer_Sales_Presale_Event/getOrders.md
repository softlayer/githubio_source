---
title: "getOrders"
description: "The orders ([SoftLayer_Billing_Order](/reference/datatypes/SoftLayer_Billing_Order)) associated with this presale event that were created for the customer's account."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Sales"
classes:
    - "SoftLayer_Sales_Presale_Event"
type: "reference"
layout: "method"
mainService : "SoftLayer_Sales_Presale_Event"
---

### [REST Example](#getOrders-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrders-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Sales_Presale_Event/{SoftLayer_Sales_Presale_EventID}/getOrders'
```
