---
title: "getAvailableNetworkStorages"
description: "Retrieves the combination of network storage devices and replicas this subnet has NOT been granted access to. Allows for filtering based on storage device type. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet"
---

### [REST Example](#getAvailableNetworkStorages-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAvailableNetworkStorages-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getAvailableNetworkStorages'
```
