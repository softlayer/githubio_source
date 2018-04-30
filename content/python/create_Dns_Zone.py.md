---
title: "create_Dns_Zone.py"
description: "create_Dns_Zone.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
"""
Create a DNS Zone.

This script creates a new domain on the SoftLayer name servers.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Sets SoftLayer API username and key.
USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Object template to create the new zone.
objectTemplate = {
                  'name': 'mydomain.com',
                  'resourceRecords': [{
                                       'data': '127.0.0.1',
                                       'host': '@',
                                       'type': 'a'
                                       }
                                      ]
                  }

# Creates a new connection to the API service.
client = SoftLayer.Client(
    username=USERNAME,
    api_key=API_KEY
)

try:
    # Creates a new domain on the SoftLayer name servers
    result = client['SoftLayer_Dns_Domain'].createObject(objectTemplate)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to create a new domain faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
