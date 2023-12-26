---
title: "createObjects"
description: "Create a new shipment tracking data. The ''shipmentId'', ''sequence'', and ''trackingData'' properties of each templateObject in the templateObjects array are required parameters to create a tracking data record. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Shipment_Tracking_Data/createObjects'
```
