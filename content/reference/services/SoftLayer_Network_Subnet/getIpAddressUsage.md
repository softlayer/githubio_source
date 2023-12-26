---
title: "getIpAddressUsage"
description: "Returns a list of IP address assignment details. Only assigned IP addresses are reported on. IP address assignments are presently only recorded and available for Primary Subnets. 

Details on the resource assigned to each IP address will only be provided to users with access to the underlying resource. If the user cannot access the resource, a detail record will still be returned for the assignment but without any accompanying resource data. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getIpAddressUsage'
```
