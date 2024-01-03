---
title: "getLoadBalancers"
description: "The virtual IP address records that belong to an application delivery controller based load balancer."
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

# [REST Example](#getLoadBalancers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLoadBalancers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/getLoadBalancers'
```
