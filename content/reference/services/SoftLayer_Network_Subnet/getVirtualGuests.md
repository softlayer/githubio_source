---
title: "getVirtualGuests"
description: "The Virtual Server devices which have been assigned a primary IP address from this subnet."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet"
---

### [REST Example](#getVirtualGuests-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVirtualGuests-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getVirtualGuests'
```
