---
title: "getEndpointSubnets"
description: "All the subnets routed to an IP address."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_IpAddress"
---

### [REST Example](#getEndpointSubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getEndpointSubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_IpAddress/{SoftLayer_Network_Subnet_IpAddressID}/getEndpointSubnets'
```
