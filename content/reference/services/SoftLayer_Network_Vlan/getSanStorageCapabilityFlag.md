---
title: "getSanStorageCapabilityFlag"
description: "A value of '1' indicates this VLAN's pod has VSI SAN disk storage capability."
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

### [REST Example](#getSanStorageCapabilityFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSanStorageCapabilityFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getSanStorageCapabilityFlag'
```
