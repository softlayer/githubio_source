---
title: "getAllCouriersByType"
description: "Retrieve a list of available shipping couriers."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Shipment"
---

### [REST Example](#getAllCouriersByType-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllCouriersByType-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment/getAllCouriersByType'
```
