---
title: "order_email_delivery_account.py"
description: "order_email_delivery_account.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Product_Order_Network_Message_Delivery"
tags:
    - "emaildelivery"
---


```
"""
Order email delivery account.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

# Build a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
# containing the order you wish to place.
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Message_Delivery",
    "packageId": 246,
    # Build a skeleton SoftLayer_Product_Item_Price object.
    # The object contains the price ID of the email delivery account
    # you wish to order.
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 13888
        }
    ],
    "accountPassword": "Testpassword1.",
    "accountUsername": "test@softlayer.com",
    "emailAddress": "test@softlayer.com"
}

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    result = productOrderService.verifyOrder(orderTemplate)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to order the email delivery account. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
