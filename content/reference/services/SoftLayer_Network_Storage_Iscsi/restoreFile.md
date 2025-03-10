---
title: "restoreFile"
description: "{{CloudLayerOnlyMethod}} Restore an individual file so that it may be used as it was before it was deleted. 

If a file is deleted from a Virtual Server Storage account, the file is placed into the account's recycle bin and not permanently deleted. Therefore, restoreFile can be used to place the file back into your Virtual Server account's root directory. "
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

### [REST Example](#restoreFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#restoreFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/restoreFile'
```
