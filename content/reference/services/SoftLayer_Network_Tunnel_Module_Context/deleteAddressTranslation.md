---
title: "deleteAddressTranslation"
description: "Remove an existing address translation from a network tunnel. 

Address translations deliver packets to a destination ip address that is on a customer subnet (remote). 

NOTE:  A network tunnel's configurations must be applied to the network device in order for an address translation to be deleted. "
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

### [REST Example](#deleteAddressTranslation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteAddressTranslation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/deleteAddressTranslation'
```
