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

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

templateObject = {
    "name": "name role",
    "description": "test user permission role"
}

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

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

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

templateObject = {
    "name": "name group",
    "description": "test group"
}

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

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

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

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

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

userGroupId = 11111

actions = [
    {
        "id": 1,  # TICKET_VIEW
    },
    {
        "id": 3,  # TICKET_ADD
    }
]

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    addBultActions = client['User_Permission_Group'].addBulkActions(actions, id=userGroupId)
    print(json.dumps(addBultActions, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add bulk actions to the user permission group faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

Link Group to the User Permission Role.

```python
import json
from pprint import pprint as pp

import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

userRoleId = 22222 

group = {
    "id": 11111
}

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

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

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

userRoleId = 22222

user = {
    "id": 11111
}

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

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

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

userId = 11111

role = {
    "id": 22222
}

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    addRole = client['User_Customer'].addRole(role, id=userId)
    print(json.dumps(addRole, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to add role to the user customer faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
