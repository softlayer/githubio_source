---
title: "get_records.py"
description: "get_records.py"
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
Get Records. Retrieve the individual records contained within a domain record

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'

# Set the domain id
# To get information the DNS Domains associated with an account, review:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
dnsId = 1769988

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    # Retrieve the individual records contained within a domain record
    result = client['SoftLayer_Dns_Domain'].getResourceRecords(id=dnsId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to get the items faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
