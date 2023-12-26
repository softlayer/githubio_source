---
title: "addAllowedHost"
description: "Use this method to attach a SoftLayer_Network_Storage_Allowed_Host object to this group.  This will automatically enable access from this host to any SoftLayer_Network_Storage volumes currently attached to this group. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Nfs"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Group_Nfs"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage_Allowed_Host]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Group_Nfs/{SoftLayer_Network_Storage_Group_NfsID}/addAllowedHost'
```
