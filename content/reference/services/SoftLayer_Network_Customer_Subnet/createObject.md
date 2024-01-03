---
title: "createObject"
description: "For IPSec network tunnels, customers can create their local subnets using this method.  After the customer is created successfully, the customer subnet can then be added to the IPSec network tunnel. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Customer_Subnet"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Customer_Subnet]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Customer_Subnet/createObject'
```
