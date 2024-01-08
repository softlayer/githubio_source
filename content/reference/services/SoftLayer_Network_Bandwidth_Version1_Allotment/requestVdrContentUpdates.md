---
title: "requestVdrContentUpdates"
description: "This will move servers into a bandwidth pool, removing them from their previous bandwidth pool and optionally remove the bandwidth pool on completion. "
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

### [REST Example](#requestVdrContentUpdates-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#requestVdrContentUpdates-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware, SoftLayer_Hardware, SoftLayer_Virtual_Guest, SoftLayer_Virtual_Guest, int, SoftLayer_Network_Application_Delivery_Controller, SoftLayer_Network_Application_Delivery_Controller]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/requestVdrContentUpdates'
```
