---
title: "getRoutableEndpointIpAddresses"
description: "Returns IP addresses which may be used as routing endpoints for a given subnet. IP address which are currently the network, gateway, or broadcast address of a Secondary Portable subnet, are an address in a Secondary Static subnet, or if the address is not assigned to a resource when part of a Primary Subnet will not be available as a routing endpoint. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getRoutableEndpointIpAddresses'
```
