---
title: "detachNetworkComponents"
description: "Detach virtual guest network components from a security group by deleting its [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding](/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding). "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_SecurityGroup"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/{SoftLayer_Network_SecurityGroupID}/detachNetworkComponents'
```
