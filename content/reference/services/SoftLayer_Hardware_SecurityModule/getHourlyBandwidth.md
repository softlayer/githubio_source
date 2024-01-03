---
title: "getHourlyBandwidth"
description: "The '''getHourlyBandwidth''' method retrieves all bandwidth updates hourly for the specified hardware. Because the potential number of data points can become excessive, the method limits the user to obtain data in 24-hour intervals. The required ''dateTime'' parameter is used as the starting point for the query and will be calculated for the 24-hour period starting with the specified date and time. For example, entering a parameter of 

'02/01/2008 0:00' 

results in a return of all bandwidth data for the entire day of February 1, 2008, as 0:00 specifies a midnight start date. Please note that the time entered should be completed using a 24-hour clock (military time, astronomical time). 

For data spanning more than a single 24-hour period, refer to the getBandwidthData function on the metricTrackingObject for the piece of hardware. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

# [REST Example](#getHourlyBandwidth-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHourlyBandwidth-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/getHourlyBandwidth'
```
