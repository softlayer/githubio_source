---
title: "createObject"
description: "Create a new address record. The ''typeId'', ''accountId'', ''description'', ''address1'', ''city'', ''state'', ''country'', and ''postalCode'' properties in the templateObject parameter are required properties and may not be null or empty. Users will be restricted to creating addresses for their account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Address"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Address"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Address]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Address/createObject'
```
