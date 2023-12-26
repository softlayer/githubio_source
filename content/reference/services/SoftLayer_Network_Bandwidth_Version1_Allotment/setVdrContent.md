---
title: "setVdrContent"
description: "This will update the bandwidth pool to the servers provided.  Servers currently in the bandwidth pool not provided on update will be removed. Servers provided on update not currently in the bandwidth pool will be added. If all servers are removed, this removes the bandwidth pool on completion. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Bandwidth_Version1_Allotment"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware, SoftLayer_Hardware, SoftLayer_Virtual_Guest, SoftLayer_Network_Application_Delivery_Controller, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/setVdrContent'
```
