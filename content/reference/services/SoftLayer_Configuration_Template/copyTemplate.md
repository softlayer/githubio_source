---
title: "copyTemplate"
description: "Copy a configuration template and returns a newly created template copy "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template"
type: "reference"
layout: "method"
mainService : "SoftLayer_Configuration_Template"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Configuration_Template]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Configuration_Template/{SoftLayer_Configuration_TemplateID}/copyTemplate'
```
