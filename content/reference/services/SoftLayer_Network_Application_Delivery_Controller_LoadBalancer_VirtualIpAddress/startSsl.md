---
title: "startSsl"
description: "Start SSL acceleration on all SSL virtual services (those with a type of HTTPS). This action should be taken only after configuring an SSL certificate for the virtual IP. "
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

### [REST Example](#startSsl-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#startSsl-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressID}/startSsl'
```
