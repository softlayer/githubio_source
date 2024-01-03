---
title: "getCurrentBillingDetail"
description: "Get the billing detail for this instance for the current billing period. This does not include bandwidth usage. "
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

# [REST Example](#getCurrentBillingDetail-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCurrentBillingDetail-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getCurrentBillingDetail'
```
