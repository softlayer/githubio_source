---
title: "getTagByTagName"
description: "Returns the Tag object with a given name. The user types in the tag name and this method returns the tag with that name. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Tag/getTagByTagName'
```
