---
title: "createObjects"
description: "Create registrations with respective registrars to associate multiple assigned subnets with the provided contact details. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Registration"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_Registration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration/createObjects'
```
