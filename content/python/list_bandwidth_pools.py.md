---
title: "list_bandwidth_pools.py"
description: "list_bandwidth_pools.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
"""
List the bandwidth pools in the account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getBandwidthAllotments
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[id, name, serviceProviderId, locationGroup[name], locationGroup, hardwareCount, privateNetworkOnlyHardwareCount, virtualGuestCount, bareMetalInstanceCount, applicationDeliveryControllerCount, totalBandwidthAllocated, outboundPublicBandwidthUsage, bandwidthAllotmentTypeId, projectedPublicBandwidthUsage]"
objectFilter = {"bandwidthAllotments": {"bandwidthAllotmentTypeId": {"operation": "!= 1"}}}

try:
    pools = []
    data = accountService.getBandwidthAllotments(mask=objectMask, filter=objectFilter)
    for item in data:
        pool = {}
        pool['name'] = item['name']
        pool['region'] = item['locationGroup']['name']
        pool['allocation'] = str(item['totalBandwidthAllocated'] / 1000) + " TB"
        if "outboundPublicBandwidthUsage" in item:
            pool['currentUsage'] = str(float(item['outboundPublicBandwidthUsage']) * 1000) + " MB"
        else:
            pool['currentUsage'] = "0 MB"
        if "projectedPublicBandwidthUsage" in item:
            pool['projectableUsage'] = str(item['projectedPublicBandwidthUsage'] * 1000) + " MB"
        else:
            pool['projectableUsage'] = "0 MB"
        pools.append(pool)
    print(json.dumps(pools, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the list. " % (e.faultCode, e.faultString))
    exit(1)

```
