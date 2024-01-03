---
title: "getFrontendIncomingBandwidth"
description: "The '''getFrontendIncomingBandwidth''' method retrieves the amount of incoming public network traffic used by a server between the given start and end date parameters. When entering the ''dateTime'' parameter, only the month, day and year of the start and end dates are required - the time (hour, minute and second) are set to midnight by default and cannot be changed. The amount of bandwidth retrieved is measured in gigabytes (GB). "
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

# [REST Example](#getFrontendIncomingBandwidth-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFrontendIncomingBandwidth-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Router/{SoftLayer_Hardware_RouterID}/getFrontendIncomingBandwidth'
```
