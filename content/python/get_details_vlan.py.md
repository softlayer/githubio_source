---
title: "get_details_vlan.py"
description: "get_details_vlan.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
"""
Retrieve VLAN details such as primary router and subnet.

Retrieve the primary router and subnet for a determinate VLAN
associated with a SoftLayer customer account
We do this with a call to the getObject() method in the
SoftLayer_Network_Vlan API service using an object mask to retrieve
associated subnets and primary router records. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The VLAN id you wish to see its details
vlanId = 557984

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkVlanService = client['SoftLayer_Network_Vlan']

"""
Declaring an object mask to get more information about the VLAN
such as the primaryRouter and the subnets
"""
objectMask = "mask[primaryRouter, subnets[ipAddresses]]"

# Send the request to get the VLAN
try:
    result = networkVlanService.getObject(id=vlanId, mask=objectMask)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get VLAN details. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
