---
title: "getCustomerManagedFlag"
description: "If false, this VIP and associated services may be edited via the portal or the API. If true, you must configure this VIP manually on the device."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---

# [REST Example](#getCustomerManagedFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCustomerManagedFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_LoadBalancer_VirtualIpAddressID}/getCustomerManagedFlag'
```
