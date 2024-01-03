---
title: "createLiveLoadBalancer"
description: "Create or add to an application delivery controller based load balancer service. The loadBalancer parameter must have its ''name'', ''type'', ''sourcePort'', and ''virtualIpAddress'' properties populated. Changes are reflected immediately in the application delivery controller. "
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

# [REST Example](#createLiveLoadBalancer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createLiveLoadBalancer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LoadBalancer_VirtualIpAddress]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/createLiveLoadBalancer'
```
