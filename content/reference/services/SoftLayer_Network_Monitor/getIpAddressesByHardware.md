---
title: "getIpAddressesByHardware"
description: "This will return an arrayObject of objects containing the ipaddresses.  Using an string parameter you can send a partial ipaddress to search within a given ipaddress.  You can also set the max limit as well using the setting the resultLimit. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Monitor"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Hardware, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Monitor/getIpAddressesByHardware'
```
