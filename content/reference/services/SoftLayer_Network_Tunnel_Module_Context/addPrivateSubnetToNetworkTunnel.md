---
title: "addPrivateSubnetToNetworkTunnel"
description: "Deprecated "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Tunnel_Module_Context"
---

### [REST Example](#addPrivateSubnetToNetworkTunnel-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addPrivateSubnetToNetworkTunnel-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/addPrivateSubnetToNetworkTunnel'
```
