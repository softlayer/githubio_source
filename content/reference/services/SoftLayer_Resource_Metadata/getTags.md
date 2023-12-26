---
title: "getTags"
description: "The getTags method retrieves all tags associated with the resource. Tags are single keywords assigned to a resource that assist the user in identifying the resource and its roles when performing a simple search. Tags are assigned by any user with access to the resource. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getTags'
```
