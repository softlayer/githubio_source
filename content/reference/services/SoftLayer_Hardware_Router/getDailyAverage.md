---
title: "getDailyAverage"
description: "The '''getDailyAverage''' method calculates the average daily network traffic used by the selected server. Using the required parameter ''dateTime'' to enter a start and end date, the user retrieves this average, measure in gigabytes (GB) for the specified date range. When entering parameters, only the month, day and year are required - time entries are omitted as this method defaults the time to midnight in order to account for the entire day. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Router"
---

### [REST Example](#getDailyAverage-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getDailyAverage-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getDailyAverage'
```
