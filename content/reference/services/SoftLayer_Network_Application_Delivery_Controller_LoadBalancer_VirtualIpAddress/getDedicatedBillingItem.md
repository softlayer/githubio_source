---
title: "getDedicatedBillingItem"
description: "The current billing item for the load balancing device housing the virtual IP. This billing item represents a device which could contain other virtual IPs. Caution should be taken when canceling. This is only valid when dedicatedFlag is true."
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

# [REST Example](#getDedicatedBillingItem-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDedicatedBillingItem-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressID}/getDedicatedBillingItem'
```
