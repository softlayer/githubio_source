---
title: "getObjectsByCredential"
description: "Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. Use this method if you wish to retrieve a storage record by a credential rather than by id. "
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

# [REST Example](#getObjectsByCredential-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObjectsByCredential-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage_Credential]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/getObjectsByCredential'
```
