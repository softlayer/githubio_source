---
title: "getCapabilities"
description: "Provides the list of capabilities a Pod fulfills. See [SoftLayer_Network_Pod::listCapabilities](/reference/services/SoftLayer_Network_Pod/listCapabilities) for more information on capabilities. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Pod"
---

### [REST Example](#getCapabilities-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCapabilities-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Pod/{SoftLayer_Network_PodID}/getCapabilities'
```
