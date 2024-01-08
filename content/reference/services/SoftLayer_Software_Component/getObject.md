---
title: "getObject"
description: "getObject retrieves the SoftLayer_Software_Component object whose ID corresponds to the ID number of the init parameter passed to the SoftLayer_Software_Component service. 

The best way to get software components is through getSoftwareComponents from the Hardware service. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component"
---

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component/{SoftLayer_Software_ComponentID}/getObject'
```
