---
title: "getPriceGroups"
description: "A location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
type: "reference"
layout: "method"
mainService : "SoftLayer_Location_Datacenter"
---

### [REST Example](#getPriceGroups-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPriceGroups-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/{SoftLayer_Location_DatacenterID}/getPriceGroups'
```
