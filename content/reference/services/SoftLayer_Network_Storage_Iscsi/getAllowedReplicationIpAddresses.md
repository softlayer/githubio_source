---
title: "getAllowedReplicationIpAddresses"
description: "The SoftLayer_Network_Subnet_IpAddress objects which are allowed access to this storage volume's Replicant."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Iscsi"
---

### [REST Example](#getAllowedReplicationIpAddresses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllowedReplicationIpAddresses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/getAllowedReplicationIpAddresses'
```
