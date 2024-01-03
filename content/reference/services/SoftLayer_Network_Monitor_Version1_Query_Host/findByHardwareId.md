---
title: "findByHardwareId"
description: "This method returns all Query_Host objects associated with the passed in hardware ID as long as that hardware ID is owned by the current user's account. 

This behavior can also be accomplished by simply tapping networkMonitors on the Hardware_Server object. "
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

# [REST Example](#findByHardwareId-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#findByHardwareId-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Monitor_Version1_Query_Host/findByHardwareId'
```
