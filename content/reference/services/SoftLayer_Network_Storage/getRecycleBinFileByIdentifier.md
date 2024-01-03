---
title: "getRecycleBinFileByIdentifier"
description: "{{CloudLayerOnlyMethod}} Retrieve the details of a file that is pending deletion in a Storage account's a recycle bin. "
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

# [REST Example](#getRecycleBinFileByIdentifier-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRecycleBinFileByIdentifier-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getRecycleBinFileByIdentifier'
```
