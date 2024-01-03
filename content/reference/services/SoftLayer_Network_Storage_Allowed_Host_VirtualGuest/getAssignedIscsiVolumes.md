---
title: "getAssignedIscsiVolumes"
description: "The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access."
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

# [REST Example](#getAssignedIscsiVolumes-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAssignedIscsiVolumes-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest/{SoftLayer_Network_Storage_Allowed_Host_VirtualGuestID}/getAssignedIscsiVolumes'
```
