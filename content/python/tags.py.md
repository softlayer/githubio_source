---
title: "Working with Tags"
description: "A few examples on interacting with Tags"

date: "2020-02-19"
classes: 
    - "SoftLayer_Tags"    
tags:
    - "Tags"
---

[Tags](https://https://sldn.softlayer.com/reference/services/SoftLayer_Tags/)

### Get all tags

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
account_service = client['Account']

try:
    response = account_service.getTags()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Autocomplete tag inputted by a user.

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

### Retrieve the account to which the tag is tied.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

tag_id = 123456

try:
    response = tag_service.getAccount(id = tag_id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get all valid tag types.

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

try:
    response = tag_service.getAllTagTypes()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### Get the tags attached to references.

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
import json

client = SoftLayer.create_client_from_env()
tag_service = client['Tag']

tag_id = 123456

try:
    response = tag_service.getReferences(id = tag_id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
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

try:
    response = tag_service.getTagByTagName()
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
tag_type = 'ACCOUNT_DOCUMENT'
resource_table_id = 1

try:
    response = tag_service.setTags(tag_name,tag_type,1)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \n \nfaultString= %s"
          % (e.faultCode, e.faultString))

```