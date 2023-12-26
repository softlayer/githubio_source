---
title: "getPossibleInsideVlans"
description: "Get all VLANs that can become inside VLANs on this gateway. This means the VLAN must not already be an inside VLAN, on the same router as this gateway, not a gateway transit VLAN, and not firewalled. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/getPossibleInsideVlans'
```
