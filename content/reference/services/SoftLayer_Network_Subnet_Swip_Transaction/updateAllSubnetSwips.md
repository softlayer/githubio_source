---
title: "updateAllSubnetSwips"
description: "
**DEPRECATED**
This method finds all subnets attached to your account that are in 'OK' status and updates their data with ARIN.  Use this function after you have updated your RWHOIS data if you want to keep SWIP up to date. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/updateAllSubnetSwips'
```
