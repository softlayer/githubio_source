---
title: "startSsl"
description: "Start SSL acceleration on all SSL virtual services (those with a type of HTTPS). This action should be taken only after configuring an SSL certificate for the virtual IP. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServerID}/startSsl'
```
