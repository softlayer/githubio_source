---
title: "deleteObject"
description: "deleteObject permanently removes a shipment tracking datum (number) "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment_Tracking_Data"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Shipment_Tracking_Data"
---

### [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment_Tracking_Data/{SoftLayer_Account_Shipment_Tracking_DataID}/deleteObject'
```
