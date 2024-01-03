---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_LoadBalancer_Service object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_LoadBalancer_Service service. You can only retrieve services on load balancers assigned to your account, and it is recommended that you simply retrieve the entire load balancer, as an individual service has no explicit purpose without its 'siblings'. "
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

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Service/{SoftLayer_Network_LoadBalancer_ServiceID}/getObject'
```
