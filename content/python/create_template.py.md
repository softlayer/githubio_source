---
title: "create_template.py"
description: "create_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device"
tags:
    - "images-templates"
---


```
"""
Create image template.

The script creates a standard image template, it makes
a call to the SoftLayer_Virtual_Guest::createArchiveTransaction method
sending the IDs of the disks in the request, the response will provide an ID property
which is the Transaction number until it´s being fully provisioned.

For more information please see below.

Important manual pages:
https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# The virtual guest ID you want to create a template
virtualGuestId = 39202937
# The name of the image template
groupName = 'fmirGroupImageTemplate'
# An optional note for the image template
note = 'an optional fmir note'

"""
Build a skeleton SoftLayer_Virtual_Guest_Block_Device object
containing the disks you want to the image.
In this case we are going take an image template of 2 disks
from the virtual machine.
"""
blockDevices = [
    {
        "id": 60788837,
        # "complexType": "SoftLayer_Virtual_Guest_Block_Device"
    },
    {
        "id": 59411427,
        # "complexType": "SoftLayer_Virtual_Guest_Block_Device"
    }
]

# Declare a new API service object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

try:
    # Creating the transaction for the image template
    response = client['SoftLayer_Virtual_Guest'].createArchiveTransaction(groupName,
                                                                          blockDevices, note, id=virtualGuestId)
    pp(response)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to create the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
