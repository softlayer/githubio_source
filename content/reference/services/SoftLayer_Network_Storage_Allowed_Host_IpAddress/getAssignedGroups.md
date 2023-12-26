---
title: "getAssignedGroups"
description: "The SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_IpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Allowed_Host_IpAddress"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host_IpAddress/{SoftLayer_Network_Storage_Allowed_Host_IpAddressID}/getAssignedGroups'
```
