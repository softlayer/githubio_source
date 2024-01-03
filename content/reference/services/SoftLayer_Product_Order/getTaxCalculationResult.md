---
title: "getTaxCalculationResult"
description: "Sometimes taxes cannot be calculated immediately, so we start the calculations and let them run in the background. This method will return the current progress and information related to a specific tax calculation, which allows real-time progress updates on tax calculations. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Order"
---

# [REST Example](#getTaxCalculationResult-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTaxCalculationResult-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/getTaxCalculationResult'
```
