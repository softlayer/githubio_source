---
title: "create_virtual_guest.py"
description: "create_virtual_guest.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Create a new Virtual Guest.
createObject() enables the creation of computing instances on an account.
This method is a simplified alternative to interacting with the ordering
system directly.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
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

orderToRequest = {
    "datacenter": {
        "name": "dal09"
        },
    "dedicatedAccountHostOnlyFlag": "true",
    "domain": "test.local",
    "hostname": "test",
    "hourlyBillingFlag": "true",
    "localDiskFlag": "false",
    "maxMemory": "1024",
    "networkComponents": [
        {
          "maxSpeed": 1000
        }
      ],
    "operatingSystemReferenceCode": "CENTOS_LATEST",
    "startCpus": "1"
    }

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

"""
To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
when you are ready to create the server call the createObject method instead.
"""
try:

    newOrder = client['Virtual_Guest'].generateOrderTemplate(orderToRequest)
    pp(newOrder)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to create a new Virtual Guest faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
