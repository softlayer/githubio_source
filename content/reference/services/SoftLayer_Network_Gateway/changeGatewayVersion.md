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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/changeGatewayVersion'
```
