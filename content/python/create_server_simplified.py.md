---
title: "create_server_simplified.py"
description: "create_server_simplified.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Create a VSI using the simplified way.

The script creates a simple VSI using the SoftLayer_Virtual_Guest::createObject method

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

"""
# To get the configuration options to create the server
# call the SoftLayer_Virtual_Guest::getCreateObjectOptions method.
# e.g.
# createOptions = virtualGuestService.getCreateObjectOptions()
# pp(createOptions)
# Creating our virtual guest server template with the configuration options that we want.
"""
templateObject = {
    "hostname": "host1",  # The name of the server
    "domain": "example.com",  # The domain for the server
    "startCpus": 2,  # The number of logical CPU cores to allocate
    "maxMemory": 2,  # The amount of memory to allocate in gigabytes.
    "localDiskFlag": False,  # Indicates that the vsi has at least one disk local to the host it runs on.
                             # This does not include a SWAP device.
    "hourlyBillingFlag": True,  # Specifies the billing type for the server.
    "operatingSystemReferenceCode": "UBUNTU_LATEST",  # An identifier for the operating system to
                                                      # provision the server with.
    "datacenter": {  # Specifies which datacenter the server is to be provisioned in.
        "name": "dal10"
        },
    "userData": [
        {
            "value": "someValue"
        }
     ]
    }

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

"""
To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
when you are ready to create the server call the createObject method instead.
"""
try:
    receipt = virtualGuestService.generateOrderTemplate(templateObject)
    pp(receipt)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    pp("Unable to create the VSI. "
          % (e.faultCode, e.faultString))

```
