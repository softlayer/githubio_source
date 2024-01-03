---
title: "findByIpv4Address"
description: "Search for an IP address record by IPv4 address."
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

# [REST Example](#findByIpv4Address-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#findByIpv4Address-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_IpAddress/findByIpv4Address'
```
