---
title: "edit_password.py"
description: "edit_password.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Software_Component_Password"
tags:
    - "managepassword"
---


```
"""
Edit a password for a device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_Password
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_Password/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Software_Component_Password/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The software component password id which contains the password.
passwordId = 8409127

username = "newUserEdit"
password = "newPassEdit"

# optional field
notes = "my optional note"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
passwordService = client['SoftLayer_Software_Component_Password']

# Build a SoftLayer_Software_Component_Password object
templatePass = {
    "username": username,
    "password": password,
    "notes": notes,
}

try:
    result = passwordService.editObject(templatePass, id=passwordId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to edit the password. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
