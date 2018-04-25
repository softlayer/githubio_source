---
title: "edit_details.py"
description: "edit_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Edit details of a Virtual Guest.
It edits a computing instance's properties


Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

serverId = 35747489

# Create an object template with data that you wish to edit.
# For example: I want to edit the "hostname" and "notes".
objectTemplate = {
    'hostname': 'myhostnameEdited',
    'notes': 'edited from api'
    }

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    # Edits an existing virtual Guest server
    # The expected result after executing the script is: true
    result = client['Virtual_Guest'].editObject(objectTemplate, id=serverId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to edit the virtual guest details faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
