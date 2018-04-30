---
title: "get_pool_details_vsis.py"
description: "get_pool_details_vsis.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
"""
Get the details for a bandwidth pool (list only the VSIs).

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# The bandwidth pool id you wish to see the details
poolId = 234419

# Declare the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[projectedPublicBandwidthUsage, datacenter, outboundPublicBandwidthUsage, bandwidthAllocation, virtualRackId, primaryIpAddress]"
objectFilter = {"virtualGuests": {"virtualRackId": {"operation": poolId}}}

try:
    details = []
    vsis = accountService.getVirtualGuests(mask=objectMask, filter=objectFilter)
    for vsi in vsis:
        detail = {}
        detail['server'] = vsi['fullyQualifiedDomainName']
        detail['ip'] = vsi['primaryIpAddress']
        detail['location'] = vsi['datacenter']['longName']
        detail['allocation'] = str(float(vsi['bandwidthAllocation']) / 1000) + " TB"
        detail['currentUsage'] = str(float(vsi['outboundPublicBandwidthUsage']) * 1000) + " MB"
        detail['projectedUsage'] = str(float(vsi['projectedPublicBandwidthUsage']) * 1000) + " MB"
        details.append(detail)
    print(json.dumps(details, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the pool details. " % (e.faultCode, e.faultString))
    exit(1)

```
