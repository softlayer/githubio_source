---
title: "editObject"
description: "The global load balancer service has been deprecated and is no longer available. 

Edit the properties of a global load balancer account by passing in a modified instance of the object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_Global_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LoadBalancer_Global_Account]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Global_Account/{SoftLayer_Network_LoadBalancer_Global_AccountID}/editObject'
```
