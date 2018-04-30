---
title: "get_subnets.py"
description: "get_subnets.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
"""
Retrieve the subnets for a VLAN

Retrieve all the subnets for a determinate VLAN
associated with a SoftLayer customer account
We do this with a call to the getSubnets() method in the
SoftLayer_Network_Vlan API service. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The VLAN id you wish to see its subnets
vlanId = 557984

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkVlanService = client['SoftLayer_Network_Vlan']

# Send the request to get the subnets
try:
    result = networkVlanService.getSubnets(id=vlanId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the subnets. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
