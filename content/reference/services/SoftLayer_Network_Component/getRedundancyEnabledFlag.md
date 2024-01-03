---
title: "getRedundancyEnabledFlag"
description: "Indicates whether the network component is participating in a group of two or more components which is actively providing link redundancy."
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

# [REST Example](#getRedundancyEnabledFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRedundancyEnabledFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/{SoftLayer_Network_ComponentID}/getRedundancyEnabledFlag'
```
