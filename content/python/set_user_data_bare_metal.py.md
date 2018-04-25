---
title: "set_user_data_bare_metal.py"
description: "set_user_data_bare_metal.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Set user data for a Bare Metal Server.

The script makes a single call to the
SoftLayer_Hardware_Server::setUserMetadata method
in order to set the user data in the bare metal server.
For more information see below.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setUserMetadata

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The id of the Bare Metal server you wish to set the user data.
baremetalId = 284776

# The user data you wish to set.
userData = ['my test']

# Declare a new API service object.
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareservice = client['SoftLayer_Hardware_Server']

try:
    result = hardwareservice.setUserMetadata(userData, id=baremetalId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to set the user data: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
