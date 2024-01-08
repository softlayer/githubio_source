---
title: "getAvailableFlag"
description: "Flag to indecate whether or not the reserved instance is available or not."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_ReservedCapacityGroup_Instance"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_ReservedCapacityGroup_Instance"
---

### [REST Example](#getAvailableFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAvailableFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_ReservedCapacityGroup_Instance/{SoftLayer_Virtual_ReservedCapacityGroup_InstanceID}/getAvailableFlag'
```
