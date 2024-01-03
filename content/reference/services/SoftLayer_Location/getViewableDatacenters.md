---
title: "getViewableDatacenters"
description: "Retrieve all datacenter locations. SoftLayer's datacenters exist in various cities and each contain one or more server rooms which house network and server infrastructure. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location"
type: "reference"
layout: "method"
mainService : "SoftLayer_Location"
---

# [REST Example](#getViewableDatacenters-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getViewableDatacenters-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location/getViewableDatacenters'
```
