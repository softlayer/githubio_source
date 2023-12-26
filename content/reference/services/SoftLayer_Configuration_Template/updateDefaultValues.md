---
title: "updateDefaultValues"
description: "Updates default configuration values. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Configuration_Template_Section_Definition_Value]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Configuration_Template/{SoftLayer_Configuration_TemplateID}/updateDefaultValues'
```
