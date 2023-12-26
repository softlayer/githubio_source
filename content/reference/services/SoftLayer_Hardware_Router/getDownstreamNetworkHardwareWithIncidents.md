---
title: "getDownstreamNetworkHardwareWithIncidents"
description: "All network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware. [DEPRECATED]"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getDownstreamNetworkHardwareWithIncidents'
```
