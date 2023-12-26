---
title: "createSubnetRouteUpdateTransaction"
description: "
***DEPRECATED***
This endpoint is deprecated in favor of the more expressive and capable SoftLayer_Network_Subnet::route, to which this endpoint now proxies. Refer to it for more information. 

Similarly, unroute requests are proxied to SoftLayer_Network_Subnet::clearRoute. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/createSubnetRouteUpdateTransaction'
```
