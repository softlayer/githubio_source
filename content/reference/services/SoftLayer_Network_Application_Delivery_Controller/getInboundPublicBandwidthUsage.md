---
title: "getInboundPublicBandwidthUsage"
description: "The total public inbound bandwidth for the current billing cycle."
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

### [REST Example](#getInboundPublicBandwidthUsage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInboundPublicBandwidthUsage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/getInboundPublicBandwidthUsage'
```