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

### [REST Example](#copyTemplate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#copyTemplate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Configuration_Template]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Configuration_Template/{SoftLayer_Configuration_TemplateID}/copyTemplate'
```
