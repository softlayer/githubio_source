---
title: "allowAccessToNetworkStorageList"
description: "This method is used to allow access to multiple SoftLayer_Network_Storage volumes that support host- or network-level access control. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_IpAddress"
---

### [REST Example](#allowAccessToNetworkStorageList-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#allowAccessToNetworkStorageList-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_IpAddress/{SoftLayer_Network_Subnet_IpAddressID}/allowAccessToNetworkStorageList'
```
