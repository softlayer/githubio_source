---
title: "getPublicVlanByFqdn"
description: "
*** DEPRECATED ***
Retrieves a public VLAN associated to the host matched by the given fully-qualified domain name. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/getPublicVlanByFqdn'
```
