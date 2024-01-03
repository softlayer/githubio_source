---
title: "getBillingCycleBandwidthUsage"
description: "A virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to."
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

# [REST Example](#getBillingCycleBandwidthUsage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBillingCycleBandwidthUsage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/getBillingCycleBandwidthUsage'
```
