---
title: "voidPendingVdrCancellation"
description: "This method will void a pending cancellation on a bandwidth pool. Note however any servers that belonged to the rack will have to be restored individually using the method voidPendingServerMove($id, $type). "
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

### [REST Example](#voidPendingVdrCancellation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#voidPendingVdrCancellation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/voidPendingVdrCancellation'
```
