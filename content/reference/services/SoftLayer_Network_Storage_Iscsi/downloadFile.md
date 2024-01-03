---
title: "downloadFile"
description: "{{CloudLayerOnlyMethod}} Download a file from a Storage account. This method returns a file's details including the file's raw content. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Iscsi"
---

# [REST Example](#downloadFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#downloadFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/downloadFile'
```
