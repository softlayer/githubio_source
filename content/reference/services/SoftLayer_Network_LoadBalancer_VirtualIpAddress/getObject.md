---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_LoadBalancer_VirtualIpAddress object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_LoadBalancer_VirtualIpAddress service. You can only retrieve Load Balancers assigned to your account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_LoadBalancer_VirtualIpAddressID}/getObject'
```
