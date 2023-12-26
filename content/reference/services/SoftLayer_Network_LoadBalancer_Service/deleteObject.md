---
title: "deleteObject"
description: "Calling deleteObject on a particular server will remove it from the load balancer.  This is the only way to remove a service from your load balancer.  If you wish to remove a server, first call this function, then reload the virtualIpAddress object and edit the remaining services to reflect the other changes that you wish to make. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_Service"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Service/{SoftLayer_Network_LoadBalancer_ServiceID}/deleteObject'
```
