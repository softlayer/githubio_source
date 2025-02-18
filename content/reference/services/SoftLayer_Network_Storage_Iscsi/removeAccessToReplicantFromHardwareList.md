---
title: "removeAccessToReplicantFromHardwareList"
description: "This method is used to modify the access control list for this Storage replica volume.  The SoftLayer_Hardware objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage replica volume. "
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

### [REST Example](#removeAccessToReplicantFromHardwareList-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAccessToReplicantFromHardwareList-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/removeAccessToReplicantFromHardwareList'
```
