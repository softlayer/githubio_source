---
title: "getFilePendingDeleteCount"
description: "{{CloudLayerOnlyMethod}} Retrieve the number of files pending deletion in a Storage account's recycle bin. Files in an account's recycle bin may either be restored to the account's root directory or permanently deleted. "
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

### [REST Example](#getFilePendingDeleteCount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFilePendingDeleteCount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getFilePendingDeleteCount'
```
