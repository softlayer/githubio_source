---
title: "createObjects"
description: "Create multiple new VLAN attachments. If the bypassFlag is false, this will also create an asynchronous process to route the VLANs through the gateway. "
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

### [REST Example](#createObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Vlan]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_Vlan/createObjects'
```
