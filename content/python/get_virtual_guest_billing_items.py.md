---
title: "get_virtual_guest_billing_items.py"
description: "get_virtual_guest_billing_items.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
tags:
    - "billing"
---


```
"""
Retrieve the billing items  for the VSI in the account.

This script makes a single call to the getVirtualGuests() method in the
SoftLayer_Account API service and uses a object mask to get the
billing items and items for each VSI server in the account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item

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

# Declaring the object mask to get information about the items.
objectMask = "mask[id, hostname, domain, datacenter[longName], billingItem[item]]"

try:
    # Retrieve the VSIs billing items for the account.
    result = accountService.getVirtualGuests(mask=objectMask)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the VSIs. " % (e.faultCode, e.faultString))
    exit(1)

```
