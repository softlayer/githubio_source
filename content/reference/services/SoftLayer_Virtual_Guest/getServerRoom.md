---
title: "getServerRoom"
description: "The server room that a guest is located at. There may be more than one server room for every data center."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### [REST Example](#getServerRoom-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServerRoom-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getServerRoom'
```
