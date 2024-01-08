---
title: "setCredentialPassword"
description: "Use this method to modify the credential password for a SoftLayer_Network_Storage_Allowed_Host object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
---

### [REST Example](#setCredentialPassword-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setCredentialPassword-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest/{SoftLayer_Network_Storage_Allowed_Host_VirtualGuestID}/setCredentialPassword'
```
