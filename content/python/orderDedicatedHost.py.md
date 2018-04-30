---
title: "orderDedicatedHost.py"
description: "orderDedicatedHost.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Location_Group_Pricing"
    - "SoftLayer_Product_Order"
tags:
    - "dedicatedhost"
---


```

"""
Order a Dedicated host.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/blog/cmporter/Location-based-Pricing-and-You
http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-3
http://sldn.softlayer.com/node/274081
http://sldn.softlayer.com/article/Python
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

orderData = {
    "orderContainers": [
        {
            "location": "DALLAS10",
            "packageId": 813,
            
            # Building a skeleton SoftLayer_Hardware_Server object to model the hostname,
            # domain and the router that we want for our dedicated host.
            "hardware": [
                {
                    "domain": "softlayer.com",
                    "hostname": "dedicastedHost",
                    "primaryBackendNetworkComponent": {
                        "router": {
                            "id": 843613
                        }
                    }
                }
            ],
            # Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            # much more than ids, but SoftLayer's ordering system only needs the price's id
            # to know what you want to order.
            # Every item in SoftLayer's product catalog is assigned an id. Use these ids
            # to tell the SoftLayer API which options you want in your new server. Use
            # the SoftLayer_Product_Package::getItemPrices method in the SoftLayer_Account
            # API service to get a list of available item and price options per available package.
            "prices": [
                {
                    "id": 200269 #  "56 Cores X 242 RAM X 1.2 TB"
                }
            ]
        }
    ]
}

try:
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderData)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
```
