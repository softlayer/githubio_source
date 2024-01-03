---
title: "getPrices"
description: "The prices that this pricing location group limits. All of these prices will only be available in the locations defined by this pricing location group."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Group_Pricing"
type: "reference"
layout: "method"
mainService : "SoftLayer_Location_Group_Pricing"
---

# [REST Example](#getPrices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Group_Pricing/{SoftLayer_Location_Group_PricingID}/getPrices'
```
