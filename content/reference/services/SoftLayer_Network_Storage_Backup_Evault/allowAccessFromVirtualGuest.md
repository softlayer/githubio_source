---
title: "allowAccessFromVirtualGuest"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Virtual_Guest objects which have been allowed access to this storage will be listed in the allowedVirtualGuests property of this storage volume. "
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

### [REST Example](#allowAccessFromVirtualGuest-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#allowAccessFromVirtualGuest-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_Guest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/allowAccessFromVirtualGuest'
```
