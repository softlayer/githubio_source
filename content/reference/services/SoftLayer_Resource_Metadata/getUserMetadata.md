---
title: "getUserMetadata"
description: "The getUserMetadata method retrieves metadata completed by users who interact with the resource. Metadata gathered using this method is unique to parameters set using the '''setUserMetadata''' method, which must be executed prior to completing this method. User metadata may also be provided while placing an order for a resource. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getUserMetadata'
```
