---
title: "getHighAvailabilityFlag"
description: "Denotes whether the virtual IP is configured within a high availability cluster."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
---

### [REST Example](#getHighAvailabilityFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHighAvailabilityFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressID}/getHighAvailabilityFlag'
```
