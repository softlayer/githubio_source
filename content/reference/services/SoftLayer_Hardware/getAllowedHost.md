---
title: "getAllowedHost"
description: "The SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

### [REST Example](#getAllowedHost-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllowedHost-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/getAllowedHost'
```
