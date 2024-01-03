---
title: "getPrimarySubnetVersion6"
description: "The primary IPv6 subnet routed on this VLAN, if IPv6 is enabled."
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

# [REST Example](#getPrimarySubnetVersion6-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPrimarySubnetVersion6-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getPrimarySubnetVersion6'
```
