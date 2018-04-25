---
title: "create_virutal_guest_tag.py"
description: "create_virutal_guest_tag.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Create a VSI using the simplified way with tags.

The script creates a simple VSI using the SoftLayer_Virtual_Guest::createObject method
along with tags.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject/
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions/
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate/
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

object_server = {
    "datacenter": {
        "name": "dal05"
    },
    "hostname": "testborrame",
    "domain": "example.com",
    "startCpus": 1,
    "maxMemory": 1024,
    "hourlyBillingFlag": True,
    "localDiskFlag": True,
    "operatingSystemReferenceCode": "UBUNTU_LATEST",
    "tagReferences":
        {
            "tag": ["mytag"]
        }
    }

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

"""
To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
when you are ready to create the server call the SoftLayer_Virtual_Guest::createObject method.
"""
try:
    result = virtualGuestService.generateOrderTemplate(object_server)
    pp (result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to create the VSI. "
          % (e.faultCode, e.faultString))

```
