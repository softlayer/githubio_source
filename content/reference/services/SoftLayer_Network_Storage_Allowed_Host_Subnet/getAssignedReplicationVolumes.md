---
title: "getAssignedReplicationVolumes"
description: "The SoftLayer_Network_Storage primary volumes whose replicas are allowed access."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Allowed_Host_Subnet"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host_Subnet/{SoftLayer_Network_Storage_Allowed_Host_SubnetID}/getAssignedReplicationVolumes'
```
