---
title: "removeFromVolume"
description: "Use this method to remove a SoftLayer_Network_Storage volume from this group.  This will automatically disable access to this volume for any SoftLayer_Network_Storage_Allowed_Host objects currently attached to this group. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Group"
---

# [REST Example](#removeFromVolume-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeFromVolume-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Group/{SoftLayer_Network_Storage_GroupID}/removeFromVolume'
```
