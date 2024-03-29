---
title: "getAttachedTagsForCurrentUser"
description: "Get all tags with at least one reference attached to it for the current account. The total items header for this method contains the total number of attached tags even if a result limit is applied. "
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

### [REST Example](#getAttachedTagsForCurrentUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAttachedTagsForCurrentUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Tag/getAttachedTagsForCurrentUser'
```
