---
title: "getInboundPublicBandwidthUsage"
description: "The total public inbound bandwidth used in this virtual rack for an account's current billing cycle."
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

### [REST Example](#getInboundPublicBandwidthUsage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInboundPublicBandwidthUsage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/getInboundPublicBandwidthUsage'
```
