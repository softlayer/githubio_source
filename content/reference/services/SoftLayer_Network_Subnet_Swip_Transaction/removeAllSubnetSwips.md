---
title: "removeAllSubnetSwips"
description: "
**DEPRECATED**
This method finds all subnets attached to your account that are in OK status and starts 'DELETE' transactions with ARIN, allowing you to remove your SWIP registration information. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Swip_Transaction"
---

### [REST Example](#removeAllSubnetSwips-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAllSubnetSwips-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/removeAllSubnetSwips'
```
