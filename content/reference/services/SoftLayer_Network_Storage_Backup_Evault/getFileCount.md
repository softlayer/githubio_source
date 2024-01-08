---
title: "getFileCount"
description: "{{CloudLayerOnlyMethod}} Retrieve the file number of files in a Virtual Server Storage account's root directory. This does not include the files stored in the recycle bin. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Backup_Evault"
---

### [REST Example](#getFileCount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFileCount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/getFileCount'
```
