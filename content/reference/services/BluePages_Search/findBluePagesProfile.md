---
title: "findBluePagesProfile"
description: "Given an IBM email address, searches BluePages and returns the employee's details. Note that this method is not available to customers, despite being visible, and will return an error response. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Search"
classes:
    - "BluePages_Search"
type: "reference"
layout: "method"
mainService : "BluePages_Search"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/BluePages_Search/findBluePagesProfile'
```
