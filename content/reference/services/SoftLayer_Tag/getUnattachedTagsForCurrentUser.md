---
title: "getUnattachedTagsForCurrentUser"
description: "Get all tags with no references attached to it for the current account. The total items header for this method contains the total number of unattached tags even if a result limit is applied. "
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

# [REST Example](#getUnattachedTagsForCurrentUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUnattachedTagsForCurrentUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Tag/getUnattachedTagsForCurrentUser'
```
