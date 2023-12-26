---
title: "getFileCount"
description: "{{CloudLayerOnlyMethod}} Retrieve the file number of files in a Virtual Server Storage account's root directory. This does not include the files stored in the recycle bin. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getFileCount'
```
