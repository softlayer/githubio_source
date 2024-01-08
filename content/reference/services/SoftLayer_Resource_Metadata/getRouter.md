---
title: "getRouter"
description: "The getRouter method will return the router associated with a network component. When the router is redundant, the hostname of the redundant group will be returned, rather than the router hostname. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
type: "reference"
layout: "method"
mainService : "SoftLayer_Resource_Metadata"
---

### [REST Example](#getRouter-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRouter-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getRouter'
```
