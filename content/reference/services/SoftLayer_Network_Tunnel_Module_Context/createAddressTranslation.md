---
title: "createAddressTranslation"
description: "Create an address translation for a network tunnel. 

To create an address translation, ip addresses from an assigned /30 static route subnet are used.  Address translations deliver packets to a destination ip address that is on a customer (remote) subnet. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for an address translation to be created. "
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

### [REST Example](#createAddressTranslation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createAddressTranslation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Tunnel_Module_Context_Address_Translation]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/createAddressTranslation'
```
