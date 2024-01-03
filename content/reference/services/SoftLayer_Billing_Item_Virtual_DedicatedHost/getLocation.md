---
title: "getLocation"
description: "The location of the billing item. Some billing items have physical properties such as the server itself. For items such as these, we provide location information."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---

# [REST Example](#getLocation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLocation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Virtual_DedicatedHost/{SoftLayer_Billing_Item_Virtual_DedicatedHostID}/getLocation'
```
