---
title: "listCapabilities"
description: "A capability is simply a string literal that denotes the availability of a feature. Capabilities are generally self describing, but any additional details concerning the implications of a capability will be documented elsewhere; usually by the Service or Operation related to it. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Pod"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Pod/listCapabilities'
```
