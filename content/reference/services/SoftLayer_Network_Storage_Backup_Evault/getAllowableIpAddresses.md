---
title: "getAllowableIpAddresses"
description: "This method retrieves a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this SoftLayer_Network_Storage. "
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

# [REST Example](#getAllowableIpAddresses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllowableIpAddresses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/getAllowableIpAddresses'
```
