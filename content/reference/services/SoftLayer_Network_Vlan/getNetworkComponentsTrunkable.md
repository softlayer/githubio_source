---
title: "getNetworkComponentsTrunkable"
description: "The viable hardware network interface trunking targets of this VLAN. Viable targets include accessible components of assigned hardware in the same pod and network as this VLAN, which are not already connected, either natively or trunked."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getNetworkComponentsTrunkable'
```
