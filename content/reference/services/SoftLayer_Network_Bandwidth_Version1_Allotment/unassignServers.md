---
title: "unassignServers"
description: "This method will reassign a collection of SoftLayer hardware to the virtual private rack "
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

### [REST Example](#unassignServers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#unassignServers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/unassignServers'
```
