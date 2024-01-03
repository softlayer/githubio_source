---
title: "route"
description: "
***DEPRECATED***
This endpoint is deprecated in favor of the more expressive and capable SoftLayer_Network_Subnet::route, to which this endpoint now proxies. Refer to it for more information. 

Similarly, unroute requests are proxied to SoftLayer_Network_Subnet::clearRoute. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress_Global"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_IpAddress_Global"
---

# [REST Example](#route-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#route-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_IpAddress_Global/{SoftLayer_Network_Subnet_IpAddress_GlobalID}/route'
```
