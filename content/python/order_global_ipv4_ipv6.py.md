---
title: "order_global_ipv4_ipv6.py"
description: "order_global_ipv4_ipv6.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
---


```
"""
Orders a new Global IPv4/IPv6 subnet

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

# Creates a new connection to the API service.
client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

# Set the package related to subnets
package_id = 0

# Filters a specific type of subnet to order e.g. GLOBAL_IPV6, GLOBAL_IPV4
filter_instance = {
    'itemPrices': {
        'item': {
            'keyName': {
                'operation': 'GLOBAL_IPV6'
            }
        }
    }
}

try:
    # Gets the item price id of selected subnet
    package_result = client['SoftLayer_Product_Package'].getItemPrices(
        id=package_id,
        filter=filter_instance)
    price_id = package_result[0]['id']

except Exception as e:
    pp('Failed ............', e)


# Order template for the Subnet order
orderTemplate = {
    'packageId': 0,
    'prices': [
        {
            'id': price_id
        }
    ],
    'quantity': 1,
    'complexType': 'SoftLayer_Container_Product_Order_Network_Subnet'
}

try:
    result = client['SoftLayer_Product_Order'].verifyOrder(orderTemplate)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to order the new item faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```
