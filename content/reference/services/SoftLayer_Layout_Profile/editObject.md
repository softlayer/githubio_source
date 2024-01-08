---
title: "editObject"
description: "This method edits an existing layout profile object by passing in a modified instance of the object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile"
type: "reference"
layout: "method"
mainService : "SoftLayer_Layout_Profile"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Layout_Profile]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Layout_Profile/{SoftLayer_Layout_ProfileID}/editObject'
```
