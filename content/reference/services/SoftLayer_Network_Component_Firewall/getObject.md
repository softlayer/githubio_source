---
title: "getObject"
description: "getObject returns a SoftLayer_Network_Firewall_Module_Context_Interface_AccessControlList_Network_Component object. You can only get objects for servers attached to your account that have a network firewall enabled. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component_Firewall"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component_Firewall/{SoftLayer_Network_Component_FirewallID}/getObject'
```
