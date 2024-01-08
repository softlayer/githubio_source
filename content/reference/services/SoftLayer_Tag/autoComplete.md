---
title: "autoComplete"
description: "This function is responsible for setting the Tags values. The internal flag is set to 0 if the user is a customer, and 1 otherwise. AccountId is set to the account bound to the user, and the tags name is set to the clean version of the tag inputted by the user. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Tag"
classes:
    - "SoftLayer_Tag"
type: "reference"
layout: "method"
mainService : "SoftLayer_Tag"
---

### [REST Example](#autoComplete-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#autoComplete-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Tag/autoComplete'
```
