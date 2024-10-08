---
title: "removeAccessToNetworkStorage"
description: "This method is used to remove access to s SoftLayer_Network_Storage volumes that supports host- or network-level access control. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### [REST Example](#removeAccessToNetworkStorage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAccessToNetworkStorage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/removeAccessToNetworkStorage'
```
