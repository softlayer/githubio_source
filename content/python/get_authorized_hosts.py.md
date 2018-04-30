---
title: "get_authorized_hosts.py"
description: "get_authorized_hosts.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Storage"
tags:
    - "endurance"
---


```
"""
Get all the authorized hosts for a iSCSI.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/getObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

iscsiId = 6548079

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkStorageService = client['SoftLayer_Network_Storage']

objectMask = "mask[id,username,allowedVirtualGuests[fullyQualifiedDomainName,allowedHost[name,credential[username,password]]],allowedHardware[fullyQualifiedDomainName,allowedHost[name,credential[username,password]]]]"

try:
    response = networkStorageService.getObject(id=iscsiId, mask=objectMask)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to retrieve the network storage. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
