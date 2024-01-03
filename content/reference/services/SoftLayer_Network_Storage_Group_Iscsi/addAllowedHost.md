---
title: "addAllowedHost"
description: "Use this method to attach a SoftLayer_Network_Storage_Allowed_Host object to this group.  This will automatically enable access from this host to any SoftLayer_Network_Storage volumes currently attached to this group. "
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

# [REST Example](#addAllowedHost-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addAllowedHost-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage_Allowed_Host]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Group_Iscsi/{SoftLayer_Network_Storage_Group_IscsiID}/addAllowedHost'
```
