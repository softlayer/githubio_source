---
title: "getAccount"
description: "The account to which the shipment belongs."
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

### [REST Example](#getAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment/{SoftLayer_Account_ShipmentID}/getAccount'
```
