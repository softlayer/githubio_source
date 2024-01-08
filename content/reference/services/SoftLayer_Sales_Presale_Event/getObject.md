---
title: "getObject"
description: "'''getObject''' retrieves the [SoftLayer_Sales_Presale_Event](/reference/datatypes/SoftLayer_Sales_Presale_Event) object whose id number corresponds to the id number of the init parameter passed to the SoftLayer_Sales_Presale_Event service. Customers may only retrieve presale events that are currently active. "
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

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Sales_Presale_Event/{SoftLayer_Sales_Presale_EventID}/getObject'
```
