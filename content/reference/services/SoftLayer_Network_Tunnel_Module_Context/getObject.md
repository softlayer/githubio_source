---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Tunnel_Module_Context object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Tunnel_Module_Context service. The IPSec network tunnel will be returned if it is associated with the account and the user has proper permission to manage network tunnels. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/getObject'
```
