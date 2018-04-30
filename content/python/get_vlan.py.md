---
title: "get_vlan.py"
description: "get_vlan.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
"""
Retrieve account VLAN and subnet information.

Retrieve a list of all VLANs associated with a SoftLayer customer account
and print a simple report detailing these VLANs and the subnets assigned to
them. We do this with a call to the getNetworkVlans() method in the
SoftLayer_Account API service using an object mask to retrieve the VLANs'
associated subnets and primary router records. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

"""
Declaring an object mask to get more information about the VLANs
such as the primaryRouter and the subnets
"""
objectMask = "mask[primaryRouter, subnets[ipAddresses]]"

# Sending the request to get the VLANs
try:
    result = accountService.getNetworkVlans(mask=objectMask)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the VLAN list. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
