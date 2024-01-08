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

### [REST Example](#updateDefaultValues-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateDefaultValues-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Configuration_Template_Section_Definition_Value]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Configuration_Template/{SoftLayer_Configuration_TemplateID}/updateDefaultValues'
```
