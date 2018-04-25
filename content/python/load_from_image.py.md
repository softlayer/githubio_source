---
title: "load_from_image.py"
description: "load_from_image.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Reload servers from a list of IPs

This script looks for a server with a determinate IP address and reload it from an image template.

Note: Regarding the Flex Image service, On Monday August 7, 2017 IBM Cloud (formerly SoftLayer)
has discontinued offering the Flex Image service.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

ipsToReload = ['159.8.52.185', '10.104.213.234']

# Call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
# to get the images templates in the account.
imageTemplateId = 1776423   # Standard Image template
                            # CentOS CentOS 7.0-64 Minimal   --- 25 GB --- 4.18 GB (Size on Disk)

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareService = client['SoftLayer_Hardware_Server']

failedServers = []
for ipToReload in ipsToReload:
    failedServer = {'ip': ipToReload}
    try:
        server = hardwareService.findByIpAddress(ipToReload)
        if server == '':
            failedServer['error'] = "Ip does not exist."
            failedServers.append(failedServer)
            continue
    except SoftLayer.SoftLayerAPIError as e:
        failedServer['error'] = e
        failedServers.append(failedServer)
        continue
    if 'activeTransaction' in server:
        failedServer['error'] = "There is an active transaction."
        failedServers.append(failedServer)
        continue

    config = {
        'imageTemplateId': imageTemplateId
    }

    try:
        reload = hardwareService.reloadOperatingSystem('FORCE', config, id=server['id'])
    except SoftLayer.SoftLayerAPIError as e:
        failedServer['error'] = e
        failedServers.append(failedServer)
        continue

print("The reload failed for these IPs:")
print(json.dumps(failedServers, sort_keys=True, indent=2, separators=(',', ': ')))

```
