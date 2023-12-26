---
title: "getServiceResource"
description: "The getServiceResource method retrieves a specific service resource associated with the resource. Service resources are additional resources that may be used by this resource. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
type: "reference"
layout: "method"
mainService : "SoftLayer_Resource_Metadata"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getServiceResource'
```
