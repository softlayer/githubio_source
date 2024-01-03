---
title: "getAvailableObjectStorageDatacenters"
description: "Object Storage is only available in select datacenters. This method will return all the datacenters where object storage is available. "
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

# [REST Example](#getAvailableObjectStorageDatacenters-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAvailableObjectStorageDatacenters-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/getAvailableObjectStorageDatacenters'
```
