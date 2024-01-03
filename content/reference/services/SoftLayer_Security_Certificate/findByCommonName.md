---
title: "findByCommonName"
description: "Locate certificates by their common name, traditionally a domain name. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate"
---

# [REST Example](#findByCommonName-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#findByCommonName-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/findByCommonName'
```
