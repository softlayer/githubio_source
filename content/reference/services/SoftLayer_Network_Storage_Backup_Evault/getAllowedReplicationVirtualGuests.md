---
title: "getAllowedReplicationVirtualGuests"
description: "The SoftLayer_Hardware objects which are allowed access to this storage volume's Replicant."
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

### [REST Example](#getAllowedReplicationVirtualGuests-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllowedReplicationVirtualGuests-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/getAllowedReplicationVirtualGuests'
```
