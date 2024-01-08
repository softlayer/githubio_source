---
title: "setGatewayPassword"
description: "Returns true if password change is successful, false if not successful 

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

### [REST Example](#setGatewayPassword-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setGatewayPassword-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/setGatewayPassword'
```
