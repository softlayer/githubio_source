---
title: "getLargestAllowedSubnetCidr"
description: "Computes the number of available public secondary IP addresses, aligned to a subnet size. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getLargestAllowedSubnetCidr-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLargestAllowedSubnetCidr-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getLargestAllowedSubnetCidr'
```
