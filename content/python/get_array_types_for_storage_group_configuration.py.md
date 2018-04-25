---
title: "get_array_types_for_storage_group_configuration.py"
description: "get_array_types_for_storage_group_configuration.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Configuration_Storage_Group_Array_Type"
tags:
    - "baremetalservers"
---


```
"""
List all the available array types for configure the storage groups.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Configuration_Storage_Group_Array_Type/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
packageService = client['SoftLayer_Configuration_Storage_Group_Array_Type']

try:
    types = packageService.getAllObjects()
    print(json.dumps(types, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("There was an error. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
