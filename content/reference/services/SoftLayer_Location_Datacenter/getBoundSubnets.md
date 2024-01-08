---
title: "getBoundSubnets"
description: "Subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
type: "reference"
layout: "method"
mainService : "SoftLayer_Location_Datacenter"
---

### [REST Example](#getBoundSubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBoundSubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/{SoftLayer_Location_DatacenterID}/getBoundSubnets'
```
