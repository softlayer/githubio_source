---
title: "editObject"
description: "Edit a bandwidth allotment's local properties. Currently you may only change an allotment's name. Use the [SoftLayer_Network_Bandwidth_Version1_Allotment::reassignServers](/reference/datatypes/$1/#$2) and [SoftLayer_Network_Bandwidth_Version1_Allotment::unassignServers](/reference/datatypes/$1/#$2) methods to move servers in and out of your allotments. "
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

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Bandwidth_Version1_Allotment]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/editObject'
```
