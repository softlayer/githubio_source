---
title: "getRoutableBoundSubnets"
description: "Retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan."
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

### [REST Example](#getRoutableBoundSubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRoutableBoundSubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/{SoftLayer_Location_DatacenterID}/getRoutableBoundSubnets'
```
