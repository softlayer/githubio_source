---
title: "getType"
description: "The type for this VLAN, with the following values: STANDARD, GATEWAY, INTERCONNECT"
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

### [REST Example](#getType-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getType-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getType'
```
