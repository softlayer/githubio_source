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

### [REST Example](#editObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_SecurityGroup]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/editObjects'
```
