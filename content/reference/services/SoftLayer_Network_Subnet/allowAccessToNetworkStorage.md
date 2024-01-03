---
title: "allowAccessToNetworkStorage"
description: "This method is used to allow access to a SoftLayer_Network_Storage volume that supports host- or network-level access control. "
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

# [REST Example](#allowAccessToNetworkStorage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#allowAccessToNetworkStorage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Storage]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/allowAccessToNetworkStorage'
```
