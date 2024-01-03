---
title: "reassignServers"
description: "This method will reassign a collection of SoftLayer hardware to a bandwidth allotment Bandwidth Pool. "
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

# [REST Example](#reassignServers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#reassignServers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/reassignServers'
```
