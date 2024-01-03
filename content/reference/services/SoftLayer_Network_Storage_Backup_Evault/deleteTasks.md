---
title: "deleteTasks"
description: "This method can be used to help maintain the storage space on a vault.  When a job is removed from the Webcc, the task and stored usage still exists on the vault. This method can be used to delete the associated task and its usage. 

All that is required for the use of the method is to pass in an integer array of task(s). 

"
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

# [REST Example](#deleteTasks-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteTasks-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/deleteTasks'
```
