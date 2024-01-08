---
title: "getAttributeByType"
description: "Retrieve a single [SoftLayer_Account_Attribute](/reference/datatypes/SoftLayer_Account_Attribute) record by its [SoftLayer_Account_Attribute_Type](/reference/datatypes/SoftLayer_Account_Attribute_Type) key name. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getAttributeByType-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAttributeByType-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getAttributeByType'
```
