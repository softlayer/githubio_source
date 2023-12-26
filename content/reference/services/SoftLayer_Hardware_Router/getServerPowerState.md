---
title: "getServerPowerState"
description: "The '''getPowerState''' method retrieves the power state for the selected server. The server's power status is retrieved from its remote management card. This method returns 'on', for a server that has been powered on, or 'off' for servers powered off. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getServerPowerState'
```
