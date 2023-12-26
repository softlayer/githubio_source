---
title: "addL7PoolMembers"
description: "Add server instances as members to a L7pool and return the LoadBalancer Object with listeners, pools and members populated "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Member"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_L7Member"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_L7Member]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Member/addL7PoolMembers'
```
