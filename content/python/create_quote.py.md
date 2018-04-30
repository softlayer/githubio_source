---
title: "create_quote.py"
description: "create_quote.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Product_Order"
tags:
    - "quotes"
---


```
"""
Create a quote.
This script creates a quote based in the information provided into the
SoftLayer_Container_Product_Order_Virtual_Guest object passing that object to
SoftLayer_Product_Order::placeQuote method.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeQuote/
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice debug output:
import pprint
"""
Your SoftLayer API username and key.
Generate an API key at the SoftLayer Customer Portal.
"""
API_USERNAME = 'set-me'
API_KEY = 'set-me'

order = {
    "orderContainers": [
        {
            "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
            "packageId": 46,
            "location": "HONGKONG02",
            "quantity": 1,
            "virtualGuests": [
                {
                    "hostname": "test",
                    "domain": "test.com"
                }
            ],
            "prices": [
                {"id": 1640},
                {"id": 1644},
                {"id": 13938},
                {"id": 2202},
                {"id": 248},
                {"id": 273},
                {"id": 2302},
                {"id": 55},
                {"id": 58},
                {"id": 420},
                {"id": 418},
                {"id": 21},
                {"id": 57},
                {"id": 905}
            ],
            "primaryDiskPartitionId": 1,
            "useHourlyPricing": False
        }
    ],
    "quoteName": "testQuote",
    "sendQuoteEmailFlag": True
}

client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

try:
    result = client['Product_Order'].placeQuote(order)
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error placing the quote, faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
