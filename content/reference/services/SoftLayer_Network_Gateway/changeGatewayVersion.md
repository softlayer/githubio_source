---
title: "changeGatewayVersion"
description: "Used to create a transaction to upgrade or rollback the vSRX version for Juniper gateway. 

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

### [REST Example](#changeGatewayVersion-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#changeGatewayVersion-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/changeGatewayVersion'
```
