---
title: "addPrivateSubnetToNetworkTunnel"
description: "Associates a private subnet to the network tunnel.  When a private subnet is associated, the network tunnel will allow the customer (remote) network to access the private subnet. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the association described above to take effect. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/addPrivateSubnetToNetworkTunnel'
```
