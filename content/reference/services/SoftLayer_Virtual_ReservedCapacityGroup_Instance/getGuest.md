---
title: "getGuest"
description: "The virtual guest associated with this reserved capacity group instance."
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

### [REST Example](#getGuest-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getGuest-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_ReservedCapacityGroup_Instance/{SoftLayer_Virtual_ReservedCapacityGroup_InstanceID}/getGuest'
```
