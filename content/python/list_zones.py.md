---
title: "list_zones.py"
description: "list_zones.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
"""
List zones

The script lists all domains belong to an account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Create a new connection to the API service.
client = SoftLayer.Client(
    username=USERNAME,
    api_key=API_KEY
)

try:
    # Get zone list through Account service
    result = client['Account'].getDomains()
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to get the items faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
