---
title: "Working with Tags"
description: "A few examples on interacting with Tags"

date: "2020-02-19"
classes: 
    - "SoftLayer_Tags"    
tags:
    - "tags"
---

[Tags](https://https://sldn.softlayer.com/reference/services/SoftLayer_Tags/)

### Get all tags

```python
import SoftLayer

client = SoftLayer.create_client_from_env()

try:
    response = client.iter_call('SoftLayer_Account', 'getTags', limit=50)
    for tag in response:
        print(tag)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Simple Tag Search.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

# Tag inputted by the user
param = 'test example'

try:
    response = tag_service.autocomplete(param)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Delete tag for a given object.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

tag_name = 'tag example'

try:
    response = tag_service.deleteTag(tag_name)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get all valid tag types.

```python
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

try:
    response = tag_service.getAllTagTypes()
    pp(response)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
| description                     | KeyName                         | Service                                           |
| -------------                   |:-------------:                  | -----:                                            |
| Hardware                        | HARDWARE                        | SoftLayer_Hardware_Server                         |
| CCI                             | GUEST                           | SoftLayer_Virtual_Guest                           |
| Ticket                          | TICKET                          | SoftLayer_Ticket                                  |
| Vlan firewall                   | NETWORK_VLAN_FIREWALL           | SoftLayer_Network_Vlan_Firewall                   |
| Image Template                  | IMAGE_TEMPLATE                  | SoftLayer_Block_Device_Template_Gruop             |
| Application Delivery Controller | APPLICATION_DELIVERY_CONTROLLER | SoftLayer_Network_Application_Delivery_Controller |
| Vlan                            | NETWORK_VLAN                    | SoftLayer_Network_Vlan                            |
| Dedicated Host                  | DEDICATED_HOST                  | SoftLayer_Virtual_DedicatedHost                   |


### Get Attached Tags.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

try:
    response = tag_service.getAttachedTagsForCurrentUser()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Retrieve a SoftLayer_Tag record.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

tag_id = 123456

try:
    response = tag_service.getObject(id=tag_id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Retrieve references that tie object to the tag.

```python
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']
tag_id = 123456
# Maps tagTypes to their correct service
reference_map = {
    'GUEST': 'SoftLayer_Virtual_Guest',
    'HARDWARE': 'SoftLayer_Hardware_Server',
    'TICKET': 'SoftLayer_Ticket',
    'NETWORK_VLAN_FIREWALL': 'SoftLayer_Network_Vlan_Firewall',
    'NETWORK_VLAN': 'SoftLayer_Network_Vlan',
    'DEDICATED_HOST': 'SoftLayer_Virtual_DedicatedHost'
}

try:
    objectMask = "mask[references[id,resourceTableId,tagType[keyName]]]"
    tag = tag_service.getObject(id=tag_id, mask=objectMask)
    for references in tag.get('references', []):
        keyname = references['tagType']['keyName']
        print( keyname +" with tag {}".format(tag.get('name')))
        object_reference = client.call(reference_map.get(keyname), 'getObject', id=references['resourceTableId'])
        pp(object_reference)
    
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get the tag object based on what the user inputs.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

# input the tag name 
tag_name = 'test name'

try:
    response = tag_service.getTagByTagName(tag_name)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get the tags not attached to references.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

try:
    response = tag_service.getUnattachedTagsForCurrentUser()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Set the tags for a given object.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

tag_name = 'tag example'

# choose the Tag type using the getTagType example 
tag_type = 'GUEST'

# resource_table_id is the id of the object you want to tag.
# Virtual_Guest id for GUEST types, Hardware_Server id for HARDWARE types, etc 
resource_table_id = 123456

try:
    response = tag_service.setTags(tag_name,tag_type,resource_table_id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```