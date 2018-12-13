---
title: "Working with user permissions"
description: "A few examples on interacting with user permissions."
date: "2018-12-12"
classes: 
    - "SoftLayer_User_Permission_Group"
    - "SoftLayer_User_Permission_Role"
    - "SoftLayer_User_Permission_Action"
tags:
    - "user"
    - "users"
    - "usercustomer"
---

Create a User Permission Role

```python
import json
from pprint import pprint as pp

import SoftLayer

templateObject = {
    "name": "name role",
    "description": "test user permission role"
}

client = SoftLayer.create_client_from_env()

try:

    createRole = client['User_Permission_Role'].createObject(templateObject)
    print(json.dumps(createRole, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to create a user permission role faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

Create a User Permission Group

```python
import json
from pprint import pprint as pp

import SoftLayer

templateObject = {
    "name": "name group",
    "description": "test group"
}

client = SoftLayer.create_client_from_env()

try:

    createGroup = client['User_Permission_Group'].createObject(templateObject)
    print(json.dumps(createGroup, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to create a user permission group faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

Retrieve the User Permission Actions e.g. TICKET_VIEW, UPDATE_PAYMENT_DETAILS, HARDWARE_VIEW, etc.

```python
import json
from pprint import pprint as pp

import SoftLayer

client = SoftLayer.create_client_from_env()

try:

    userPermissionActions = client['User_Permission_Action'].getAllObjects()
    print(json.dumps(userPermissionActions, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to retrieve the user permission actions faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```

Add Bulk Actions to the User Permission Group.

```python
import json
from pprint import pprint as pp

import SoftLayer

userGroupId = 11111

actions = [
    {
        "id": 1,  # TICKET_VIEW
    },
    {
        "id": 3,  # TICKET_ADD
    }
]

client = SoftLayer.create_client_from_env()

try:
    addBultActions = client['User_Permission_Group'].addBulkActions(actions, id=userGroupId)
    print(json.dumps(addBultActions, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add bulk actions to the user permission group faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

Add Resouce Object (Virtual_Guest) to the User Permission Group

```python
import json
from pprint import pprint as pp

import SoftLayer

groupId = 11111

resourceObject = {
        "complexType": "SoftLayer_Virtual_Guest",
         "id":"22222"
      }

client = SoftLayer.create_client_from_env()

try:
    resourceObject = client['SoftLayer_User_Permission_Group'].addResourceObject(resourceObject, id=groupId)
    print(json.dumps(resourceObject, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add resouce object to the user permission group faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

Add Resouce Object (Hardware_Server) to the User Permission Group

```python
import json
from pprint import pprint as pp

import SoftLayer

groupId = 11111

resourceObject = {
        "complexType": "SoftLayer_Hardware_Server",
         "id":"22222"
      }

client = SoftLayer.create_client_from_env()

try:
    resourceObject = client['SoftLayer_User_Permission_Group'].addResourceObject(resourceObject, id=groupId)
    print(json.dumps(resourceObject, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add resource object to the user permission group faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```


Link Group to the User Permission Role.

```python
import json
from pprint import pprint as pp

import SoftLayer

userRoleId = 22222 

group = {
    "id": 11111
}

client = SoftLayer.create_client_from_env()

try:
    linkGroup = client['User_Permission_Role'].linkGroup(group, id=userRoleId)
    print(json.dumps(linkGroup, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to link group to the user permission role faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```


Add User to the User Permission Role.

```python
import json
from pprint import pprint as pp

import SoftLayer

userRoleId = 22222

user = {
    "id": 11111
}

client = SoftLayer.create_client_from_env()

try:
    addUser = client['User_Permission_Role'].addUser(user, id=userRoleId)
    print(json.dumps(addUser, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add user to the user permission role faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

Add Role to the User Customer.

```python
import json
from pprint import pprint as pp

import SoftLayer

userId = 11111

role = {
    "id": 22222
}

client = SoftLayer.create_client_from_env()

try:
    addRole = client['User_Customer'].addRole(role, id=userId)
    print(json.dumps(addRole, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add role to the user customer faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
