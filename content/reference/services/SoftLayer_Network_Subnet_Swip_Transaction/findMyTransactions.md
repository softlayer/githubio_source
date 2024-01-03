---
title: "findMyTransactions"
description: "
**DEPRECATED**
This function will return an array of SoftLayer_Network_Subnet_Swip_Transaction objects, one for each SWIP that is currently in transaction with ARIN.  This includes all swip registrations, swip removal requests, and SWIP objects that are currently OK. "
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

# [REST Example](#findMyTransactions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#findMyTransactions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/findMyTransactions'
```
