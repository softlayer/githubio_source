---
title: "deleteObjects"
description: "Detach several VLANs. This will not detach them right away, but rather start an asynchronous process to detach. "
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

# [REST Example](#deleteObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Vlan]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_Vlan/deleteObjects'
```
