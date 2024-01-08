---
title: "editObject"
description: "Edit the properties of a media record by passing in a modified instance of a SoftLayer_Account_Media object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Media"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Media"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Media]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Media/{SoftLayer_Account_MediaID}/editObject'
```
