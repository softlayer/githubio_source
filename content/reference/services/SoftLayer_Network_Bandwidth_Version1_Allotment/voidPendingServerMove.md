---
title: "voidPendingServerMove"
description: "This method will void a pending server removal from this bandwidth pooling. Pass in the id of the hardware object or virtual guest you wish to update. Assuming that object is currently pending removal from the bandwidth pool at the start of the next billing cycle, the bandwidth pool member status will be restored and the pending cancellation removed. "
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

# [REST Example](#voidPendingServerMove-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#voidPendingServerMove-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/voidPendingServerMove'
```
