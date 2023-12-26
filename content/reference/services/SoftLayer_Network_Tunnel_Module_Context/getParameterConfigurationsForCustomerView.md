---
title: "getParameterConfigurationsForCustomerView"
description: "All of the IPSec VPN tunnel's configurations will be returned.  It will list all of phase one and two negotiation parameters.  Both remote and local subnets will be provided as well.  This is useful when the configurations need to be passed on to another team and/or company for internal network configuration. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/getParameterConfigurationsForCustomerView'
```
