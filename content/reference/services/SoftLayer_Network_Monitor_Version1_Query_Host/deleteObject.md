---
title: "deleteObject"
description: "Like any other API object, the monitoring objects can be deleted by passing an instance of them into this function.  The ID on the object must be set. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Monitor_Version1_Query_Host"
---

# [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Monitor_Version1_Query_Host/{SoftLayer_Network_Monitor_Version1_Query_HostID}/deleteObject'
```
