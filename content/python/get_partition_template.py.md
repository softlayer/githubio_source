---
title: "get_partition_template.py"
description: "get_partition_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Component_Partition_OperatingSystem"
tags:
    - "baremetalservers"
---


```
"""
List the partition templates available for the first disk.
The partition templates available will depend on the OS selected and the disk type assigned.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem/getByDescription
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Component_Partition_OperatingSystem/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'Set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'Set-me'

# To get the valid list of description values use
# SoftLayer_Hardware_Component_Partition_OperatingSystem::getAllObjects method.
description = "linux"

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
packageService = client['SoftLayer_Hardware_Component_Partition_OperatingSystem']

objectMask = "mask[partitionTemplates[data]]"

try:
    templates = packageService.getByDescription(description, mask=objectMask)
    print(json.dumps(templates, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the partition templates. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
