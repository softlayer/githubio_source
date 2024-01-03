---
title: "createObject"
description: "Create a secondary DNS record. The ''zoneName'', ''masterIpAddress'', and ''transferFrequency'' properties in the templateObject parameter are required parameters to create a secondary DNS record. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Secondary"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Secondary]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/createObject'
```
