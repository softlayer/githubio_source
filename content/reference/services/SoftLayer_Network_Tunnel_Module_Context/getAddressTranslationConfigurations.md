---
title: "getAddressTranslationConfigurations"
description: "The address translations will be returned.  All the translations will be formatted so that the configurations can be copied into a host file. 

Format: 

{address translation SoftLayer IP Address}        {address translation name} "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/getAddressTranslationConfigurations'
```
