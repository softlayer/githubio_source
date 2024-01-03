---
title: "removeMediaFromList"
description: "Remove a media from a SoftLayer account's list of media. The media record is not deleted. "
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

# [REST Example](#removeMediaFromList-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeMediaFromList-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Media]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Media/removeMediaFromList'
```
