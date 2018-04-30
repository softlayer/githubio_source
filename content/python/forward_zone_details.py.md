---
title: "forward_zone_details.py"
description: "forward_zone_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
"""
DNS Forward Zone Details

The script shows the DNS Forward Zone Details.This means, that this retrieves
the individual records contained within a domain record

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Set SoftLayer API username and key.
USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Set the forward zone id
dnsId = 1769988

# Create a new connection to the API service.
client = SoftLayer.Client(
    username=USERNAME,
    api_key=API_KEY
)

# Filter data according to details displayed in Customer Portal.
filterInstance = {"resourceRecords": {"type": {"operation": "soa"}}}

try:
    # Gets the Forward Zone Details
    result = client['SoftLayer_Dns_Domain'].getResourceRecords(
        id=dnsId, filter=filterInstance)
    pp(result)
except Exception as e:
    # An error message will be displayed if something is wrong in the script
    pp('Failed ............', e)

```
