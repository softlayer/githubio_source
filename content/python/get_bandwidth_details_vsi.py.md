---
title: "get_bandwidth_details_vsi.py"
description: "get_bandwidth_details_vsi.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "bandwidthpools"
---


```
"""
Get the bandwidth details for a server.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object
http://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/getSummaryData
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Metric_Tracking_Object

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json
import datetime

USERNAME = 'set me'
API_KEY = 'set me'

vsiId = 9066729

startDate = "2015-10-3"
endDate = "2015-10-10"
summaryPeriod = 3600

types = [
    {
        "keyName": "PUBLICIN",
        "name": "publicIn",
        "summaryType": "sum"
    },
    {
        "keyName": "PUBLICOUT",
        "name": "publicOut",
        "summaryType": "sum"
    }
]

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']
metricService = client['SoftLayer_Metric_Tracking_Object']

objectMask = "mask[metricTrackingObjectId]"

try:
    trackMetric = vsiService.getObject(mask=objectMask, id=vsiId)
    result = metricService.getSummaryData(startDate, endDate, types, summaryPeriod, id=trackMetric['metricTrackingObjectId'])
    startDay = (datetime.datetime.strptime(result[0]['dateTime'][:22] + result[0]['dateTime'][23:], "%Y-%m-%dT%H:%M:%S%z")).day
    sumCounterIn = 0
    sumCounterOut = 0
    report = []
    oldDate = (datetime.datetime.strptime(result[0]['dateTime'][:22] + result[0]['dateTime'][23:], "%Y-%m-%dT%H:%M:%S%z"))
    i = 0
    while i < len(result):
        dt = datetime.datetime.strptime(result[i]['dateTime'][:22] + result[i]['dateTime'][23:], "%Y-%m-%dT%H:%M:%S%z")
        record = {}
        record['day'] = oldDate.strftime('%Y-%m-%d')
        record['in'] = str(sumCounterIn / 1048576) + " MB"
        record['out'] = str(sumCounterOut / 1048576) + " MB"
        record['total'] = str((sumCounterIn + sumCounterOut) / 1048576) + " MB"
        if startDay == dt.day:
            sumCounterIn = sumCounterIn + result[i]['counter']
            sumCounterOut = sumCounterOut + result[i+1]['counter']
        else:
            report.append(record)
            startDay = dt.day
            sumCounterIn = result[i]['counter']
            sumCounterOut = result[i+1]['counter']
        oldDate = dt
        i = i + 2
    report.append(record)
    print(json.dumps(report, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the bandwidth details. " % (e.faultCode, e.faultString))
    exit(1)

```
