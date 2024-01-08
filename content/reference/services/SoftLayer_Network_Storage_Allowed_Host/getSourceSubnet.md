---
title: "getSourceSubnet"
description: "Connections to a target with a source IP in this subnet prefix are allowed."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Allowed_Host"
---

### [REST Example](#getSourceSubnet-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSourceSubnet-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host/{SoftLayer_Network_Storage_Allowed_HostID}/getSourceSubnet'
```
