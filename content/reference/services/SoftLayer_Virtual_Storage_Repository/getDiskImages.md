---
title: "getDiskImages"
description: "The [SoftLayer_Virtual_Disk_Image](/reference/datatypes/SoftLayer_Virtual_Disk_Image) that are in a storage repository. Disk images are the virtual hard drives for a virtual guest."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Storage_Repository"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Storage_Repository/{SoftLayer_Virtual_Storage_RepositoryID}/getDiskImages'
```
