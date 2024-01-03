---
title: "getNetworkVlansTrunkable"
description: "The viable trunking targets of this component. Viable targets include accessible VLANs in the same pod and network as this component, which are not already natively attached nor trunked to this component."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component"
---

# [REST Example](#getNetworkVlansTrunkable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNetworkVlansTrunkable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/{SoftLayer_Network_ComponentID}/getNetworkVlansTrunkable'
```
