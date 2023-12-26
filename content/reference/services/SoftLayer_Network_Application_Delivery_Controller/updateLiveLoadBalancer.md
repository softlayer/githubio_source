---
title: "updateLiveLoadBalancer"
description: "Update the the virtual IP address interface within an application delivery controller based load balancer identified by the ''name'' property in the loadBalancer parameter. You only need to set the properties in the loadBalancer parameter that you wish to change. Any virtual IP properties omitted or left empty are ignored. Changes are reflected immediately in the application delivery controller. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LoadBalancer_VirtualIpAddress]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/updateLiveLoadBalancer'
```
