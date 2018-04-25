---
title: "list_servers.py"
description: "list_servers.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
"""
List Bare Metal servers.

The script retrieve a list of all bare metal servers in your
account. it makes a single call to the Softlayer_Account::getHardware
method for more information see below.

Important manual pages:
https://sldn.softlayer.com/reference/services/SoftLayer_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
https://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# Create a SoftLayer API client object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)


"""
We will retrieve the additional information
for each server:
primaryIpAddress, primaryBackendIpAddress,
datacenter, datacenterName, serviceProvider,
hardwareFunctionDescription
"""
object_mask = 'primaryIpAddress, primaryBackendIpAddress, datacenter,' \
              'datacenterName, serviceProvider, hardwareFunctionDescription'


try:
    # getHardware() will get all the bare metal servers that an account has.
    hardwareList = client['SoftLayer_Account'].getHardware(mask=object_mask)
    pp(hardwareList)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the bare metal servers: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
