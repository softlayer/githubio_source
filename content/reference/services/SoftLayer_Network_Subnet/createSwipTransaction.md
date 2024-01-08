---
title: "createSwipTransaction"
description: "
***DEPRECATED***
This function is used to create a new SoftLayer SWIP transaction to register your RWHOIS data with ARIN. SWIP transactions can only be initiated on subnets that contain more than 8 IP addresses. "
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

### [REST Example](#createSwipTransaction-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createSwipTransaction-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/createSwipTransaction'
```
