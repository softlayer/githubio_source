---
title: "unbypassVlans"
description: "Start the asynchronous process to unbypass the provided VLANs. The VLANs must already be attached. Any VLANs that are already unbypassed will be ignored. The status field can be checked for progress. "
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

# [REST Example](#unbypassVlans-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#unbypassVlans-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Vlan]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/unbypassVlans'
```
