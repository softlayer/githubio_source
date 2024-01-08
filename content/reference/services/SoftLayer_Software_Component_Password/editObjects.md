---
title: "editObjects"
description: "Edit more than one password from a software component. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_Password"
---

### [REST Example](#editObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Software_Component_Password]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_Password/editObjects'
```
