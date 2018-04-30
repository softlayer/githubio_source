---
title: "get_billing_info.py"
description: "get_billing_info.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Info"
    - "SoftLayer_Account"
tags:
    - "billing"
---


```
"""
Retrieve the billing info for the Bare Metals in the account.

This script makes a single call to the getHardware() method in the
SoftLayer_Account API service and uses a object mask to get the
billing info for each Bare Metal server in the account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Info

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Client configuration
Your SoftLayer API username and key.
"""
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Declaring the object mask to get information about the billing item.
objectMask = "mask[id, hostname, domain, datacenter[longName], billingItem[recurringFee]]"

try:
    # Retrieve the bare metal servers for the account.
    result = accountService.getHardware(mask=objectMask)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the servers. " % (e.faultCode, e.faultString))
    exit(1)

```
