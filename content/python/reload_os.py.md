---
title: "reload_os.py"
description: "reload_os.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Reload servers from a list of IPs

This script looks for a server with a determinate IP address and reloads
the Operative System with another one.

It makes a single call to the reloadOperatingSystem() method in the
SoftLayer_Hardware_Server API service

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The IP addresses you wish to reload
ipsToReload = ['159.8.52.190']

# The new OS you wish to load
newOSToLoad = 'CentOS 6.x - Minimal Install (64 bit)'


# Declare a new API service objects for: SoftLayer_Hardware_Server
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareService = client['SoftLayer_Hardware_Server']

"""
Add an object mask to retrieve our prices related to the servers
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
for a list of the relational properties you can retrieve along with hardware.
"""
objectMask = "mask[billingItem[package[items[prices]]]]"

# the list of servers to reload
serversToReload = {}

"""
We are looking for the server with the specified IP addresses
and the price for the new OS to load
"""
try:
    for ipToReload in ipsToReload:
        server = hardwareService.findByIpAddress(ipToReload, mask=objectMask)
        serversToReload[ipToReload] = {}
        serversToReload[ipToReload]['id'] = server['id']
        if 'billingItem' in server.keys():
            for item in server["billingItem"]["package"]["items"]:
                if item['description'] == newOSToLoad:
                    serversToReload[ipToReload]['priceId'] = item['prices'][0]['id']
                    break
    # we are calling the reloadOperatingSystem for the desired servers
    for ipToReload in ipsToReload:
        config = {
            'itemPrices': [
                {
                    'id': serversToReload[ipToReload]['id']
                }
                ]
            }
        reload = hardwareService.reloadOperatingSystem('FORCE', config, id=serversToReload[ipToReload]['id'])
        print(reload)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to reload the bare metal servers: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
