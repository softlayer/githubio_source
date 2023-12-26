---
title: "createObject"
description: "Create a new VLAN attachment. If the bypassFlag is false, this will also create an asynchronous process to route the VLAN through the gateway. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway_Vlan"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Vlan]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_Vlan/createObject'
```
