---
title: "getCancelFailureReasons"
description: "Evaluates this VLAN for cancellation and returns a list of descriptions why this VLAN may not be cancelled. If the result is empty, this VLAN may be cancelled. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getCancelFailureReasons'
```
