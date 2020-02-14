---
title: "Working with Network_Pod"
description: "A few examples on interacting with Network Pod"

date: "2020-01-22"
classes: 
    - "SoftLayer_Network_Pod"    
tags:
    - "Network_Pod"
---

[Network_Pod](https://https://sldn.softlayer.com/reference/services/SoftLayer_Network_Pod/)

### Get the all Metric Pod

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
network_pod_service = client['Network_Pod']

try:
    response = network_pod_service.getAllObjects()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get the all Metric Pod using filters

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
network_pod_service = client['Network_Pod']

# Filter by datacenter name
objectFilter={"datacenterName":{"operation": "ams01"}}

try:
    response = network_pod_service.getAllObjects(filter=objectFilter)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get the network pod capabilities

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
network_pod_service = client['Network_Pod']

# name =  datacenter name . pod name
name = "ams01.pod01"

try:
    response = network_pod_service.getCapabilities(id=name)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get the network pod object

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
network_pod_service = client['Network_Pod']

# name =  datacenter name . pod name
name = "ams01.pod01"

try:
    response = network_pod_service.getObject(id=name)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Get the list capabilities network pod

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
network_pod_service = client['Network_Pod']

# name =  datacenter name . pod name 
name = "ams01.pod01"

try:
    response = network_pod_service.listCapabilities(id=name)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
