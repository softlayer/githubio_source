---
title: "isPingable"
description: "The '''isPingable''' method issues a ping command to the selected server and returns the result of the ping command. This boolean return value displays ''true'' upon successful ping or ''false'' for a failed ping. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/isPingable'
```
