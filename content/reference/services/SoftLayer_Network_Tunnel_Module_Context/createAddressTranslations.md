---
title: "createAddressTranslations"
description: "This has the same functionality as the SoftLayer_Network_Tunnel_Module_Context::createAddressTranslation.  However, it allows multiple translations to be passed in for creation. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the address translations to be created. "
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

# [REST Example](#createAddressTranslations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createAddressTranslations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Tunnel_Module_Context_Address_Translation]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/createAddressTranslations'
```
