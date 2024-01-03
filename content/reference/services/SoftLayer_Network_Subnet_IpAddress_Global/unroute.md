---
title: "unroute"
description: "
***DEPRECATED***
This endpoint is deprecated in favor of SoftLayer_Network_Subnet::clearRoute, to which this endpoint now proxies. Refer to it for more information. "
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

# [REST Example](#unroute-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#unroute-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_IpAddress_Global/{SoftLayer_Network_Subnet_IpAddress_GlobalID}/unroute'
```
