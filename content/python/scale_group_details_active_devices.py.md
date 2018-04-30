---
title: "scale_group_details_active_devices.py"
description: "scale_group_details_active_devices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "scalegroups"
---


```
"""
Get the scale group details (devices).

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

scaleGroupId = 595465

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMaskMember = "mask[datacenter,scaleMember]"
objectFilterMember = {"virtualGuests": {"scaleMember": {"scaleGroupId": {"operation": scaleGroupId}}}}

objectFilterAssets = {"virtualGuests": {"scaleAssets": {"scaleGroupId": {"operation": scaleGroupId}}}}
objectMaskAssets = "mask[datacenter,scaleAssets]"

try:
    items = accountService.getVirtualGuests(mask=objectMaskMember, filter=objectFilterMember)
    members = []
    for item in items:
        member = {}
        member['deviceName'] = item['fullyQualifiedDomainName']
        member['location'] = item['datacenter']['longName']
        member['publicIp'] = item['primaryIpAddress']
        member['privateIp'] = item['primaryBackendIpAddress']
        member['startDate'] = item['createDate']
        members.append(member)
    items = accountService.getVirtualGuests(mask=objectMaskAssets, filter=objectFilterAssets)
    assets = []
    for item in items:
        asset = {}
        asset['deviceName'] = item['fullyQualifiedDomainName']
        asset['location'] = item['datacenter']['longName']
        asset['publicIp'] = item['primaryIpAddress']
        asset['privateIp'] = item['primaryBackendIpAddress']
        asset['startDate'] = item['createDate']
        assets.append(asset)
    config = {}
    config['members'] = members
    config['assets'] = assets
    print(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the scale group details. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
