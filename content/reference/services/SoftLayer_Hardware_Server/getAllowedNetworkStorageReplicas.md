---
title: "getAllowedNetworkStorageReplicas"
description: "The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getAllowedNetworkStorageReplicas'
```
