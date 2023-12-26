---
title: "findAllSubnetsAndActiveSwipTransactionStatus"
description: "
***DEPRECATED***
Retrieve a list of a SoftLayer customer's subnets along with their SWIP transaction statuses. This is a shortcut method that combines the SoftLayer_Network_Subnet retrieval methods along with [[object masks]] to retrieve their subnets' associated SWIP transactions as well. 

This is a special function built for SoftLayer's use on the SWIP section of the customer portal, but may also be useful for API users looking for the same data. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/findAllSubnetsAndActiveSwipTransactionStatus'
```
