---
title: "list_upgrade_prices.py"
description: "list_upgrade_prices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Get list of prices to upgrade VSI.

The script retrieves the list of items to upgrade an arbitrary VSI.
for more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getUpgradeItemPrices
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

virtualGuestID = 35747489

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

try:
    result = virtualGuestService.getUpgradeItemPrices(True, id=virtualGuestID)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to list the prices to upgrade. "
          % (e.faultCode, e.faultString))

```
