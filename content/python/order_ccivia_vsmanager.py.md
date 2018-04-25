---
title: "order_ccivia_vsmanager.py"
description: "order_ccivia_vsmanager.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Create a VSI using VSManager class.

The script Verifies an instance creation command without actually placing an order.
When ready to order change the manager to create_instance instead of verify_create_instance, remember
that this will incur in billing charges.

For more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject/
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
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

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

mgr = SoftLayer.VSManager(client)

try:
    result = mgr.verify_create_instance(cpus=4, memory=2048, domain='24hsb.com',
                                        hostname="redhat-x86-64", datacenter='wdc01',
                                        os_code="UBUNTU_LATEST", disks = ('100','25'),
                                        local_disk=True)

    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to create the VSI. "
          % (e.faultCode, e.faultString))

```
