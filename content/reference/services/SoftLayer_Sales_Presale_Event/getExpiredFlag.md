---
title: "getExpiredFlag"
description: "A flag to indicate that the presale event is expired. A presale event is expired if the current time is after the end date."
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

# [REST Example](#getExpiredFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getExpiredFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Sales_Presale_Event/{SoftLayer_Sales_Presale_EventID}/getExpiredFlag'
```
