---
title: "getBoundRouters"
description: "The list of network routers that this subnet is directly associated with, defining where this subnet may be routed on the network."
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

### [REST Example](#getBoundRouters-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBoundRouters-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getBoundRouters'
```
