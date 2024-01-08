---
title: "setTags"
description: "Tag an object by passing in one or more tags separated by a comma. Tag references are cleared out every time this method is called. If your object is already tagged you will need to pass the current tags along with any new ones. To remove all tag references pass an empty string. To remove one or more tags omit them from the tag list. The characters permitted are A-Z, 0-9, whitespace, _ (underscore), - (hypen), . (period), and : (colon). All other characters will be stripped away. You must pass 3 string arguments into this method or you will receive an exception. "
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

### [REST Example](#setTags-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setTags-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Tag/setTags'
```
