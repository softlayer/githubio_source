---
title: "get_reverse_domain_records.py"
description: "get_reverse_domain_records.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
tags:
    - "subnets"
---


```
"""
Get Reverse Domain Records

The script list retrieves all reverse DNS records associated with a subnet.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getSubnetForIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getReverseDomainRecords

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

ipAddress = '119.81.70.176'

# Create a new connection to the API service.
client = SoftLayer.Client(
    username=USERNAME,
    api_key=API_KEY
)

try:
    # Get subnet zone list through SoftLayer_Network_Subnet service
    subnetResult = client['SoftLayer_Network_Subnet'].getSubnetForIpAddress(
        ipAddress)
    subnetId = subnetResult['id']

    try:
        # Get reverse domain records information
        result = client['SoftLayer_Network_Subnet'].getReverseDomainRecords(
            id=subnetId)
        pp(result)
    except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get reverse domain records information faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the subnet information faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
