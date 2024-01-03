---
title: "getCurrentBillingTotal"
description: "Get the total bill amount in US Dollars ($) for this instance in the current billing period. This includes all bandwidth used up to the point this method is called on the instance. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#getCurrentBillingTotal-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCurrentBillingTotal-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getCurrentBillingTotal'
```
