---
title: "get_object.py"
description: "get_object.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
"""
Get Hardware

This script retrieves the SoftLayer_Hardware object whose ID number corresponds
to the ID number of the init parameter passed to the SoftLayer_Hardware service.
You can only retrieve the account that your portal user is assigned to.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware

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
packageService = client['SoftLayer_Hardware']

packageId = 308926

try:
    presets = packageService.getObject(id=packageId)
    print(json.dumps(presets, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the presets for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
