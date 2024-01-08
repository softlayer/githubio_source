---
title: "attachToVolume"
description: "Use this method to attach a SoftLayer_Network_Storage volume to this group.  This will automatically enable access to this volume for any SoftLayer_Network_Storage_Allowed_Host objects currently attached to this group. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Iscsi"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Group_Iscsi"
---

### [REST Example](#attachToVolume-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#attachToVolume-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Group_Iscsi/{SoftLayer_Network_Storage_Group_IscsiID}/attachToVolume'
```
