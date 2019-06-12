---
title: "Working with CDN Network.py"
description: "A few examples on interacting with CDN Network"

date: "2019-06-11"
classes: 
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"    
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"    
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"    
tags:
    - "cdn"
---

### List CDN network

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()

apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']


try:
    response = apiAuthenticationKey.listDomainMappings()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the CDN network: ",
          '{} - {}'.format(e.faultCode, e.faultString))          
```

###list CDN origin path

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path']

"""
Set with CDN unique id. 
"""
uniqueId = "123456"

try:
    response = apiAuthenticationKey.listOriginPath(uniqueId)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for CDN origin path: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 

```

###  Detail CDN by UniqueId

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

"""
Set with CDN unique id. 
"""
uniqueId = "123456"

try:
    response = apiAuthenticationKey.listDomainMappingByUniqueId(uniqueId)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to show the response for the CDN network detail: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 
```

### Create CDN Network

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

body_json = {
    "cname": "test.cdnedge.bluemix.net",
    "domain": "www.techsupport3.com",
    "httpPort": 80,
    "origin": "10.10.10.5",
    "originType": "HOST_SERVER",
    "vendorName": "akamai",
    "header": "www.test.com",
    "path": "/test",
    "protocol": "HTTP"
}

try:
    response = apiAuthenticationKey.createDomainMapping(body_json)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to show the response for create CDN network: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 

```
### Create CDN Origin Path

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path']

"""
uniqueId your change with you unique ID.
"""

body_json = {
    "certificateType": "SHARED_SAN_CERT",
    "httpPort": 80,
    "origin": "10.10.10.3",
    "originType": "HOST_SERVER",
    "vendorName": "akamai",
    "header": "www.test.com",
    "path": "/test",
    "domain": "www.test.com",
    "protocol": "HTTP",
    "performanceConfiguration": "General web delivery",
    "uniqueId": "111111111"
}

try:
    response = apiAuthenticationKey.createOriginPath(body_json)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to show the response for the CDN network: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 

```

### Delete CDN by uniqueID
```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

uniqueId='set me'

try:
    response = apiAuthenticationKey.deleteDomainMapping(uniqueId)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to show the response for the CDN network: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 
```

### Delete CDN origin path
```python

import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path']

"""
Set with CDN unique id and the path. 
"""
uniqueId = "set me"
path = "/test/*"

try:
    response = apiAuthenticationKey.deleteOriginPath(uniqueId,path)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
   print("Unable to show the response for the CDN network: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 
```

### Purge CDN

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
apiAuthenticationKey = client['SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge']

"""
Set with CDN unique id and the path. 
"""
uniqueId = "set me"
path = "/test"

try:
    response = apiAuthenticationKey.createPurge(uniqueId,path)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to show the response for the CDN network: ",
          '{} - {}'.format(e.faultCode, e.faultString)) 
```