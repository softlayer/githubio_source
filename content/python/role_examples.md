---
title: "Role Examples"
description: "Examples of how Roles works"
date: "2019-04-09"
classes: 
    - "SoftLayer_User_Permission_Role"
    - "SoftLayer_User_Permission_Group"
    - "SoftLayer_User_Permission_Action"
tags:
    - "user"
    - "usercustomer"
---

In order to create the roles and assign them the permissions these are the steps you could to follow:

* Working with roles
  1.  [Create a Role](#step-1-create-a-role) 
  2.  [Create a Group](#step-2-create-a-group) 
  3. [Assign actions to the Group](#step-3-assign-actions-to-the-group)
  4. [Link the Group to the Role](#step-4-link-the-group-to-the-role)
  5. [Add user to the Role](#step-5-add-user-to-the-role)
* [Adding resources]( #adding-resources )
* [Edit Role](#edit-role)
* [Delete Role](#delete-role)

## Working with Roles
### Step 1: Create a Role

```python
from pprint import pprint

import SoftLayer

templateObject = {
    "name": "name role",
    "description": "test user permission role"
}

client = SoftLayer.create_client_from_env()

try:

    createRole = client['User_Permission_Role'].createObject(templateObject)
    pprint(createRole)

except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to create a user permission role :{}, {}'
           .format(e.faultCode, e.faultString))

```

### Step 2: Create a Group

```python
from pprint import pprint

import SoftLayer

templateObject = {
    "name": "GroupName",
    "description": "test group"
}

client = SoftLayer.create_client_from_env()

try:

    createGroup = client['User_Permission_Group'].createObject(templateObject)
    pprint(createGroup)

except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to create a user permission group: {}, {}'
           .format(e.faultCode, e.faultString))
```

### Step 3: Assign actions to the Group

```python
import SoftLayer
from pprint import pprint


class Group:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()

    def add_permission(self, group_init, keynames):
        bulk_actions = self.gather_actions(keynames)
        result = self.client['User_Permission_Group'].addBulkActions(bulk_actions, id=group_init)
        pprint(result)

    def gather_actions(self, keynames):
        """Retrieve the permissions from keyname list"""
        actions_list = []
        # Retrieve all available permissions
        permissions = self.client['User_Permission_Action'].getAllObjects()
        for permission in permissions:
            if permission['keyName'] in keynames:
                actions_list.append({'id': permission['id']})
        return actions_list


if __name__ == "__main__":
    main = Group()
    actions = [
        'TICKET_VIEW',
        'TICKET_EDIT',
        'TICKET_ADD',
        'HARDWARE_VIEW'
    ]
    # The user permission group id on which will be added permissions.
    group_id =  16727456
    main.add_permission(group_id, actions)
    
```
### Step 4: Link the Group to the Role

```python
from pprint import pprint

import SoftLayer

roleId = 12345

group = {
    "id": 12345678
}

client = SoftLayer.create_client_from_env()

try:
    linkGroup = client['User_Permission_Role'].linkGroup(group, id=roleId)
    pprint(linkGroup)

except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to link group to the user permission :{}, {}'
           .format(e.faultCode, e.faultString))

```

### Step 5: Add user to the Role

```python
from pprint import pprint

import SoftLayer

roleId = 12345

user = {
    "id": 11111
}

client = SoftLayer.create_client_from_env()

try:
    addUser = client['User_Permission_Role'].addUser(user, id=roleId)
    pprint(addUser)

except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to add user to the user permission role : {}, {}'
           .format(e.faultCode, e.faultString))

```
## Adding resources 
Resources Objects are added by using [SoftLayer_User_Permission_Group::addResourceObject](https://sldn.softlayer.com/reference/services/SoftLayer_User_Permission_Group/addResourceObject/)


Add Virtual_Guest 

```python
from pprint import pprint

import SoftLayer

groupId = 12345678

resourceObject = {
    "complexType": "SoftLayer_Virtual_Guest",
    "id": "22222"
}

client = SoftLayer.create_client_from_env()

try:
    resourceObject = client['SoftLayer_User_Permission_Group'].addResourceObject(resourceObject, id=groupId)
    pprint(resourceObject)

except SoftLayer.SoftLayerAPIError as e:
    pprint('Unable to add resource object to the user permission group : {}, {}'
           .format(e.faultCode, e.faultString))
```

Add Hardware_Server

```python
from pprint import pprint

import SoftLayer

groupId = 12345678

resourceObject = {
    "complexType": "SoftLayer_Hardware_Server",
    "id": "22222"
}

client = SoftLayer.create_client_from_env()

try:
    resourceObject = client['SoftLayer_User_Permission_Group'].addResourceObject(resourceObject, id=groupId)
    pprint(resourceObject)

except SoftLayer.SoftLayerAPIError as e:
    pprint(('Unable to add resource object to the user permission group :{}, {}'
            .format(e.faultCode, e.faultString)))
```
## Edit Role
```python
import SoftLayer

from pprint import pprint

roleId = 12345

client = SoftLayer.create_client_from_env()

roleTemplate = {
    'description': 'role update',
    'name': 'role-test',
}
try:
    editedRole = client['SoftLayer_User_Permission_Role'].editObject(roleTemplate, id=roleId)
    pprint(editedRole)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to edit role: ",
          '{} - {}'.format(e.faultCode, e.faultString))
```
## Delete Role
```python
import SoftLayer

from pprint import pprint

roleId = 12345

client = SoftLayer.create_client_from_env()

try:
    editedRole = client['SoftLayer_User_Permission_Role'].deleteObject(id=roleId)
    pprint(editedRole)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete role: ",
          '{} - {}'.format(e.faultCode, e.faultString))

```