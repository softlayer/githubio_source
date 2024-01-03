---
title: "removeAccessToNetworkStorageList"
description: "This method is used to allow access to multiple SoftLayer_Network_Storage volumes that support host- or network-level access control. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#removeAccessToNetworkStorageList-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAccessToNetworkStorageList-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/removeAccessToNetworkStorageList'
```
