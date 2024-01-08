---
title: "updateLoadBalancerProtocols"
description: "Update (create) load balancers front- and backend protocols and return load balancer object with listeners (frontend), pools (backend), server instances (members) and datacenter populated. Note if a protocolConfiguration has no listenerUuid set, this function will create the specified front- and backend accordingly. Otherwise the given front- and backend will be updated with the new protocol and port. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Listener"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_Listener"
---

### [REST Example](#updateLoadBalancerProtocols-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateLoadBalancerProtocols-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_Listener/updateLoadBalancerProtocols'
```
