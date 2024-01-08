---
title: "credentialDelete"
description: "Delete a credential "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
---

### [REST Example](#credentialDelete-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#credentialDelete-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage_Credential]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Hub_Cleversafe_Account/{SoftLayer_Network_Storage_Hub_Cleversafe_AccountID}/credentialDelete'
```
