---
title: "getVlanForIpAddress"
description: "Retrieves the VLAN on which the given IP address is routed."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan"
---

# [REST Example](#getVlanForIpAddress-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVlanForIpAddress-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/getVlanForIpAddress'
```
