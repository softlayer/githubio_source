---
title: "removeServiceSubnetFromNetworkTunnel"
description: "Disassociate a service subnet from a network tunnel.  When a service subnet is disassociated, that customer (remote) subnet on the other end of the network tunnel will not able to communicate with that service subnet on the SoftLayer network. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the disassociation described above to take effect. "
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

# [REST Example](#removeServiceSubnetFromNetworkTunnel-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeServiceSubnetFromNetworkTunnel-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/removeServiceSubnetFromNetworkTunnel'
```
