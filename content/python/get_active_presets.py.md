---
title: "get_active_presets.py"
description: "get_active_presets.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Package_Preset"
tags:
    - "baremetalservers"
---


```
"""
List the active presets for a package.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getActivePresets
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Preset/

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
packageService = client['SoftLayer_Product_Package']

packageId = 200

try:
    presets = packageService.getActivePresets(id=packageId)
    print(json.dumps(presets, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the presets for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
