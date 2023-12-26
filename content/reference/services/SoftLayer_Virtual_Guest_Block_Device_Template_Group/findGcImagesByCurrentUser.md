---
title: "findGcImagesByCurrentUser"
description: "Find block device template groups containing a GC enabled cloudinit image for the current active user. A sorted collection of groups is returned. The Caller can optionally specify data center or region names to retrieve GC images from only those locations. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/findGcImagesByCurrentUser'
```
