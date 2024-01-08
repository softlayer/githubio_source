---
title: "swipAllSubnets"
description: "
**DEPRECATED**
swipAllSubnets finds all subnets attached to your account and attempts to create a SWIP transaction for all subnets that do not already have a SWIP transaction in progress. "
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

### [REST Example](#swipAllSubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#swipAllSubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/swipAllSubnets'
```
