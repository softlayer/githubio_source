---
title: "countHourlyInstances"
description: "Retrieve the number of hourly services on an account that are active, plus any pending orders with hourly services attached. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

# [REST Example](#countHourlyInstances-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#countHourlyInstances-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/countHourlyInstances'
```
