---
title: "getGraphImage"
description: "Get the graph image for a load balancer service based on the supplied graph type and metric.  The available graph types are: 'connections' and 'status', and the available metrics are: 'day', 'week' and 'month'. 

This method returns the raw binary image data. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Service/{SoftLayer_Network_LoadBalancer_ServiceID}/getGraphImage'
```
