---
title: "deleteLiveLoadBalancerService"
description: "Remove an entire load balancer service, including all virtual IP addresses, from and application delivery controller based load balancer. The ''name'' property the and ''name'' property within the ''vip'' property of the service parameter must be provided. Changes are reflected immediately in the application delivery controller. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LoadBalancer_Service]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/deleteLiveLoadBalancerService'
```
