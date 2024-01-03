---
title: "addCustomerSubnetToNetworkTunnel"
description: "Associates a remote subnet to the network tunnel.  When a remote subnet is associated, a network tunnel will allow the customer (remote) network to communicate with the private and service subnets on the SoftLayer network which are on the other end of this network tunnel. 

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

# [REST Example](#addCustomerSubnetToNetworkTunnel-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addCustomerSubnetToNetworkTunnel-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/addCustomerSubnetToNetworkTunnel'
```
