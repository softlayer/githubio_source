---
title: "getAllowedReplicationSubnets"
description: "The SoftLayer_Network_Subnet objects which are allowed access to this storage volume's Replicant."
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

### [REST Example](#getAllowedReplicationSubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllowedReplicationSubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/getAllowedReplicationSubnets'
```
