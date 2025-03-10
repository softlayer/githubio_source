---
title: "getFileByIdentifier"
description: "{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date of a file within a Storage account. This does not download file content. "
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

### [REST Example](#getFileByIdentifier-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFileByIdentifier-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/getFileByIdentifier'
```
