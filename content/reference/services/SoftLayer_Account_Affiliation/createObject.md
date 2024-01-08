---
title: "createObject"
description: "Create a new affiliation to associate with an existing account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Affiliation"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Affiliation"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Affiliation]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Affiliation/createObject'
```
