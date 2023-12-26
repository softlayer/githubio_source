---
title: "toggleManagementInterface"
description: "Attempt to toggle the IPMI interface.  If there is an active transaction on the server, it will throw an exception. This method creates a job to toggle the interface.  It is not instant. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/toggleManagementInterface'
```
