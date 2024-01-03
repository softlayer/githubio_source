---
title: "getSecondarySubnets"
description: "All non-primary subnets routed on this VLAN."
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

# [REST Example](#getSecondarySubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSecondarySubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getSecondarySubnets'
```
