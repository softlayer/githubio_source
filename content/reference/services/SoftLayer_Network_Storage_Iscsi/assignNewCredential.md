---
title: "assignNewCredential"
description: "This method will set up a new credential for the remote storage volume. The storage volume must support an additional credential. Once created, the credential will be automatically assigned to the current volume. If there are no volumes assigned to the credential it will be automatically deleted. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/assignNewCredential'
```
