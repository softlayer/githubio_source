---
title: "downloadAddressTranslationConfigurations"
description: "Provides all of the address translation configurations for an IPSec VPN tunnel in a text file "
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

### [REST Example](#downloadAddressTranslationConfigurations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#downloadAddressTranslationConfigurations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/downloadAddressTranslationConfigurations'
```
