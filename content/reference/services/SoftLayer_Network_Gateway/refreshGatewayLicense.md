---
title: "refreshGatewayLicense"
description: "Used to refresh the license for the Juniper Gateway, requires License readiness check has passed. 

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

### [REST Example](#refreshGatewayLicense-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#refreshGatewayLicense-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/refreshGatewayLicense'
```
