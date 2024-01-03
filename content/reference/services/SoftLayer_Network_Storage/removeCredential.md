---
title: "removeCredential"
description: "This method will remove a credential from the current volume. The credential must have been created using the 'addNewCredential' method. "
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

# [REST Example](#removeCredential-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeCredential-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/removeCredential'
```
