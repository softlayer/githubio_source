---
title: "editObject"
description: "Edit the properties of a shipment record by passing in a modified instance of a SoftLayer_Account_Shipment_Item object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Shipment_Item"
---

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Shipment_Item]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment_Item/{SoftLayer_Account_Shipment_ItemID}/editObject'
```
