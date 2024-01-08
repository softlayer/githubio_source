---
title: "getPrivateVlanByIpAddress"
description: "
*** DEPRECATED ***
Retrieve the private network VLAN associated with an IP address. "
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

### [REST Example](#getPrivateVlanByIpAddress-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrivateVlanByIpAddress-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress'
```
