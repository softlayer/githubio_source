---
title: "getLiveLoadBalancerServiceGraphImage"
description: "Get the graph image for an application delivery controller service based on the supplied graph type and metric.  The available graph types are: 'connections' and 'status', and the available metrics are: 'day', 'week' and 'month'. 

This method returns the raw binary image data. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LoadBalancer_Service, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/getLiveLoadBalancerServiceGraphImage'
```
