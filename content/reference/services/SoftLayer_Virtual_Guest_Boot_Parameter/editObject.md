---
title: "editObject"
description: "Edits a single boot parameter"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Boot_Parameter"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest_Boot_Parameter"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_Guest_Boot_Parameter]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Boot_Parameter/{SoftLayer_Virtual_Guest_Boot_ParameterID}/editObject'
```
