---
title: "getRoutingTypeKeyName"
description: "The product and route classifier for this routed subnet, with the following values: PRIMARY, SECONDARY, STATIC_TO_IP, GLOBAL_IP, IPSEC_STATIC_NAT."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getRoutingTypeKeyName'
```
