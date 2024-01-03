---
title: "bypassAllVlans"
description: "Start the asynchronous process to bypass all VLANs. Any VLANs that are already bypassed will be ignored. The status field can be checked for progress. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---

# [REST Example](#bypassAllVlans-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#bypassAllVlans-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/bypassAllVlans'
```
