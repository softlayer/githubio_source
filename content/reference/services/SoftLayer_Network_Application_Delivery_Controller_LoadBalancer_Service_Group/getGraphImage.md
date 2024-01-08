---
title: "getGraphImage"
description: "Get the graph image for a load balancer service group based on the supplied graph type and metric.  The only available graph type currently is: 'connections', and the available metrics are: 'day', 'week' and 'month'. 

This method returns the raw binary image data. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group"
---

### [REST Example](#getGraphImage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getGraphImage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_GroupID}/getGraphImage'
```
