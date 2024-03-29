---
title: "getAllBackbones"
description: "Retrieve a list of all SoftLayer backbone connections. Use this method if you need all backbones or don't know the id number of a specific backbone. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Backbone"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Backbone"
---

### [REST Example](#getAllBackbones-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllBackbones-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Backbone/getAllBackbones'
```
