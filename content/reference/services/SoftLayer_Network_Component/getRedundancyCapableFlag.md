---
title: "getRedundancyCapableFlag"
description: "Indicates whether the network component is participating in a group of two or more components capable of being operationally redundant, if enabled."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component"
---

### [REST Example](#getRedundancyCapableFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRedundancyCapableFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/{SoftLayer_Network_ComponentID}/getRedundancyCapableFlag'
```
