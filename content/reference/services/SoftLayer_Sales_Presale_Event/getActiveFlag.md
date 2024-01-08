---
title: "getActiveFlag"
description: "A flag to indicate that the presale event is currently active. A presale event is active if the current time is between the start and end dates."
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

### [REST Example](#getActiveFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getActiveFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Sales_Presale_Event/{SoftLayer_Sales_Presale_EventID}/getActiveFlag'
```
