---
title: "getOnlineSslVpnUserCount"
description: "The total number of users online using SoftLayer's SSL VPN service for a location."
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

### [REST Example](#getOnlineSslVpnUserCount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOnlineSslVpnUserCount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/{SoftLayer_Location_DatacenterID}/getOnlineSslVpnUserCount'
```
