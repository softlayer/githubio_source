---
title: "order_static_public_subnet_ipv6.py"
description: "order_static_public_subnet_ipv6.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
---


```
"""
Orders a new Static Public IPv6

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

API_USERNAME = 'set me'
API_KEY = 'set me'

# Order Template with all new item configurations
orderTemplate = {
    'packageId': 0,
    'endPointIpAddressId': 18263116,
    'prices': [
        {
            'id': 1481
        }
    ],
    'quantity': 1,
    'complexType': 'SoftLayer_Container_Product_Order_Network_Subnet'
}

# Creates a new connection to the API service.
client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    result = client['SoftLayer_Product_Order'].verifyOrder(orderTemplate)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to order the new item faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```
