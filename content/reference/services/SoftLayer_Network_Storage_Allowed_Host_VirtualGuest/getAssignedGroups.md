---
title: "getAssignedGroups"
description: "The SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in."
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

### [REST Example](#getAssignedGroups-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAssignedGroups-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest/{SoftLayer_Network_Storage_Allowed_Host_VirtualGuestID}/getAssignedGroups'
```
