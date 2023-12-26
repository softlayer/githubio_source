---
title: "editObject"
description: "Edit the properties of a tracking data record by passing in a modified instance of a SoftLayer_Account_Shipment_Tracking_Data object. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Shipment_Tracking_Data]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment_Tracking_Data/{SoftLayer_Account_Shipment_Tracking_DataID}/editObject'
```
