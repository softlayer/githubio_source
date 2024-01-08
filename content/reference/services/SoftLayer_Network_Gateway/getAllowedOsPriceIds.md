---
title: "getAllowedOsPriceIds"
description: "Used to get a list of OS prices (ids) which are allowed for the Gateway. 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---

### [REST Example](#getAllowedOsPriceIds-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllowedOsPriceIds-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/getAllowedOsPriceIds'
```
