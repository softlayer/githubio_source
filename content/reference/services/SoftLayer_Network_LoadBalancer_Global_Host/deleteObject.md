---
title: "deleteObject"
description: "The global load balancer service has been deprecated and is no longer available. 

Remove a host from the load balancing pool of a global load balancer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Host"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_Global_Host"
---

### [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Global_Host/{SoftLayer_Network_LoadBalancer_Global_HostID}/deleteObject'
```
