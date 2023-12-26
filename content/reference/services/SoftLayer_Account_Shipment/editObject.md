---
title: "editObject"
description: "Edit the properties of a shipment record by passing in a modified instance of a SoftLayer_Account_Shipment object. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Shipment]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment/{SoftLayer_Account_ShipmentID}/editObject'
```
