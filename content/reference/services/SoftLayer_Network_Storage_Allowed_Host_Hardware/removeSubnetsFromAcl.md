---
title: "removeSubnetsFromAcl"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Allowed_Host_Hardware"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host_Hardware/{SoftLayer_Network_Storage_Allowed_Host_HardwareID}/removeSubnetsFromAcl'
```
