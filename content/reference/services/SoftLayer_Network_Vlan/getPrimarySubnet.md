---
title: "getPrimarySubnet"
description: "A primary IPv4 subnet routed on this VLAN, if accessible."
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

# [REST Example](#getPrimarySubnet-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrimarySubnet-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getPrimarySubnet'
```
