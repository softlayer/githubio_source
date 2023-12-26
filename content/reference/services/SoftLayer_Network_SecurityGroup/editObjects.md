---
title: "editObjects"
description: "Edit security groups."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_SecurityGroup"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_SecurityGroup]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/editObjects'
```
