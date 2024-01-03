---
title: "getEndpointsWithRefetch"
description: "Returns a collection of endpoint URLs available to this IBM Cloud Object Storage account. "
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

# [REST Example](#getEndpointsWithRefetch-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getEndpointsWithRefetch-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Hub_Cleversafe_Account/{SoftLayer_Network_Storage_Hub_Cleversafe_AccountID}/getEndpointsWithRefetch'
```
