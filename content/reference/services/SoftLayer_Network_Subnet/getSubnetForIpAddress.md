---
title: "getSubnetForIpAddress"
description: "Retrieve the subnet associated with an IP address. You may only retrieve subnets assigned to your SoftLayer customer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet"
---

# [REST Example](#getSubnetForIpAddress-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSubnetForIpAddress-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/getSubnetForIpAddress'
```
