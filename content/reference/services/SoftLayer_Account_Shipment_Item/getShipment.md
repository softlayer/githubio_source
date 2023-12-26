---
title: "getShipment"
description: "The shipment to which this item belongs."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment_Item/{SoftLayer_Account_Shipment_ItemID}/getShipment'
```
