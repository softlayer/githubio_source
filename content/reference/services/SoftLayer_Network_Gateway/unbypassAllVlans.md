---
title: "unbypassAllVlans"
description: "Start the asynchronous process to unbypass all VLANs. Any VLANs that are already unbypassed will be ignored. The status field can be checked for progress. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/unbypassAllVlans'
```
