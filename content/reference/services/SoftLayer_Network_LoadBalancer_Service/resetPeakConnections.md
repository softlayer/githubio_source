---
title: "resetPeakConnections"
description: "Calling resetPeakConnections will set the peakConnections variable to zero on this particular object. Peak connections will continue to increase normally after this method call, it will only temporarily reset the statistic to zero, until the next time it is polled. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_Service"
---

# [REST Example](#resetPeakConnections-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#resetPeakConnections-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Service/{SoftLayer_Network_LoadBalancer_ServiceID}/resetPeakConnections'
```
