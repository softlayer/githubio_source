---
title: "get_metric.py"
description: "get_metric.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "graphs"
---


```
"""
Get Metric

The script gets the CPU Metric and Memory Metric for a VSI
for more information see below

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCpuMetricDataByDate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricDataByDate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Your SoftLayer API username and key.

Generate an API key at the SoftLayer Customer Portal:
https://manage.softlayer.com/Administrative/apiKeychain
"""
USERNAME = 'set me'
API_KEY = 'set me'

# The virtual guest ID you want to reload
virtualGuestId = 4949592

startDateTime = "2014-06-04T00:00:00-05:00"
endDateTime = "2014-07-14T10:37:00-05:00"

# Declare a new API service object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Getting the metrics
    cpuMetrict = client['SoftLayer_Virtual_Guest'].getCpuMetricDataByDate(startDateTime, endDateTime, id=virtualGuestId)
    print(cpuMetrict)
    memoryMetrict = client['SoftLayer_Virtual_Guest'].getMemoryMetricDataByDate(startDateTime, endDateTime, id=virtualGuestId)
    print(memoryMetrict)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to get metrics faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
