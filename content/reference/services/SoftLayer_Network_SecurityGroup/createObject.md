---
title: "createObject"
description: "Create a new security group."
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

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_SecurityGroup]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/createObject'
```
