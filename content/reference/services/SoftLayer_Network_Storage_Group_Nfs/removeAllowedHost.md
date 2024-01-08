---
title: "removeAllowedHost"
description: "Use this method to remove a SoftLayer_Network_Storage_Allowed_Host object from this group.  This will automatically disable access from this host to any SoftLayer_Network_Storage volumes currently attached to this group. "
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

### [REST Example](#removeAllowedHost-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAllowedHost-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage_Allowed_Host]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Group_Nfs/{SoftLayer_Network_Storage_Group_NfsID}/removeAllowedHost'
```
