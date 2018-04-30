---
title: "get_subnet_details.py"
description: "get_subnet_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet"
tags:
    - "subnets"
---


```
"""
Get subnet details. It retrieves information related to a subnet.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnets

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
subnetId = 555920

# Object mask helps to get more and specific information related to the item
objectMask = 'id,broadcastAddress,networkVlan.primaryRouter.attributes.hardwareAttributeType'

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    result = client['SoftLayer_Network_Subnet'].getObject(id=subnetId, mask=objectMask)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the subnet information faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
