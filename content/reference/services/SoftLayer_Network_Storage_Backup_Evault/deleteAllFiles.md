---
title: "deleteAllFiles"
description: "{{CloudLayerOnlyMethod}} Delete all files within a Storage account. Depending on the type of Storage account, Deleting either deletes files permanently or sends files to your account's recycle bin. 

Currently, Virtual Server storage is the only type of Storage account that sends files to a recycle bin when deleted. When called against a Virtual Server storage account , this method also determines if the files are in the account's recycle bin. If the files exist in the recycle bin, then they are permanently deleted. 

Please note, files can not be restored once they are permanently deleted. "
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

### [REST Example](#deleteAllFiles-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteAllFiles-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/deleteAllFiles'
```
