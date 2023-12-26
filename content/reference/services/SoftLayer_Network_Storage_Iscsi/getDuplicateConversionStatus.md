---
title: "getDuplicateConversionStatus"
description: "This method is used to check, if for the given classic file block storage volume, a transaction performing dependent to independent duplicate conversion is active. If yes, then this returns the current percentage of its progress along with its start time as [SoftLayer_Container_Network_Storage_DuplicateConversionStatusInformation] object with its name, percentage and transaction start timestamp. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/getDuplicateConversionStatus'
```
