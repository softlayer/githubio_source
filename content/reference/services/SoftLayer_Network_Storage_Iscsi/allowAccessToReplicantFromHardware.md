---
title: "allowAccessToReplicantFromHardware"
description: "This method is used to modify the access control list for this Storage replicant volume.  The SoftLayer_Hardware objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage replicant volume. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/allowAccessToReplicantFromHardware'
```
