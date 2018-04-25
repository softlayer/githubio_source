---
title: "delete_domain_resource_record.py"
description: "delete_domain_resource_record.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Account"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
"""
Delete Record.

This script deletes a domain's resource record. The deleteObject method returns
Boolean true on successful deletion

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains

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

# Set a domain ID
# To get Domain information: http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
recordId = 1801053

# Create a new connection to the API service.
client = SoftLayer.Client(
    username=USERNAME,
    api_key=API_KEY
)


try:
    # Delete a domain's resource record
    result = client['SoftLayer_Dns_Domain_ResourceRecord'].deleteObject(
        id=recordId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    # An error message will be displayed if something is wrong in the script
    pp('Failed ... Unable to delete the item faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
