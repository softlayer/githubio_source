---
title: "Working with Metric_Tracking_Object"
description: "A few examples on interacting with Metric tracking object"

date: "2019-12-20"
classes: 
    - "SoftLayer_Metric_Tracking_Object"    
tags:
    - "metric_tracking"
---

[Metric_Tracking_Object](https://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/)

### Get the all metric tracking ids

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
account_service = client['Account']

mask = 'id,metricTrackingObject[id]'

try:
    response = account_service.getVirtualGuests(mask = mask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get bandwidth data

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

startDate = '2019-07-09T19:06:11-06:00'
endDate = '2019-07-09T19:06:11-16:00'

body = 'public'

"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'

try:
    response = metric_service.getBandwidthData(startDate, endDate, body, id = id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
### Get custom graph data

```python
import SoftLayer

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

body = {
    "baseUnit": "",
    "endDatetime": "2019-07-09T19:06:11-06:00",
    "metrics": [{
        "keyName": "VIRTUAL_DEDICATED_RACK",
        "name": "Bandwidth Allotment",
        "unit": "unit"}
]}

"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'

try:
    response = metric_service.getCustomGraphData(body, id = id)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
### Get details for date range

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

startDate = '2019-07-09T19:06:11-06:00'
endDate = '2019-07-09T19:06:11-16:00'

body = ['InstanceCount','HostMemoryUsage']

"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'

try:
    response = metric_service.getDetailsForDateRange(startDate, endDate, body, id = id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get metric data types

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'

try:
    response = metric_service.getMetricDataTypes(id = id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get object

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'

try:
    response = metric_service.getObject(id = id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get summary data

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

startDate = '2019-07-09T19:06:11-06:00'
endDate = '2019-07-09T19:06:11-16:00'

body = [{
    'keyName': 'CPU0',
    'summaryType': 'max'},
    {
        'keyName': 'MEMORY_USAGE',
        'summaryType': 'max'},
    {
        'keyName': 'CPU1',
        'summaryType': 'max'},
    {
        'keyName': 'CPU2',
        'summaryType': 'max'},
    {
        'keyName': 'CPU3',
        'summaryType': 'max'
    }]
    
"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'    

try:
    response = metric_service.getSummaryData(startDate,
                                              endDate, body, 600, id = id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get Metric Tracking Object type

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
metric_service = client['Metric_Tracking_Object']

"""
Set with Metric_Tracking_Object id. 
"""
id = '123456'

try:
    response = metric_service.getType(id = id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
