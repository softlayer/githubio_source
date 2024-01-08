---
title: "getBackendIncomingBandwidth"
description: "The '''getBackendIncomingBandwidth''' method retrieves the amount of incoming private network traffic used between the given start date and end date parameters. When entering start and end dates, only the month, day and year are used to calculate bandwidth totals - the time (HH:MM:SS) is ignored and defaults to midnight. The amount of bandwidth retrieved is measured in gigabytes. "
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

### [REST Example](#getBackendIncomingBandwidth-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBackendIncomingBandwidth-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getBackendIncomingBandwidth'
```
