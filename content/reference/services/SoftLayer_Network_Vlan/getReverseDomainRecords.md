---
title: "getReverseDomainRecords"
description: "
*** DEPRECATED ***
Retrieves DNS PTR records associated with IP addresses routed on this VLAN. Results will be grouped by DNS domain with the 'resourceRecords' property populated. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getReverseDomainRecords'
```
