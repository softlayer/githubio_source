---
title: "unroute_global_ip.py"
description: "unroute_global_ip.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress_Global"
    - "SoftLayer_Network_Subnet"
tags:
    - "subnets"
---


```
"""
Route Global IP. This function is used to create a new transaction
to unroute a global IP address
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress_Global/route
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

subnetId = 880579

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)


try:
    # Get the Global IP record
    globalIpRecord = client['SoftLayer_Network_Subnet'].getGlobalIpRecord(
        id=subnetId)
    pp(globalIpRecord)
    globalIpRecordId = globalIpRecord['id']
    pp(globalIpRecordId)
    try:
        # Unroute a global IP address
        result = client['SoftLayer_Network_Subnet_IpAddress_Global'].unroute(
            id=globalIpRecordId)
        pp(result)
    except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to unroute the global IP address faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to Global IP record faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```
