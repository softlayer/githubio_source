---
title: "place_order_evault.py"
description: "place_order_evault.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
tags:
    - "evault"
---


```
"""
Order a Evault

Build a SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
object for a new Evault order and pass it to the SoftLayer_Product_Order
for more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain
"""

USERNAME = 'set me'
API_KEY = 'set me'

# Create a SoftLayer API client object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['Product_Order']

orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault",

    # Build a skeleton SoftLayer_Hardware object.
    # The object contains the hardware ID of the
    # Bare Metal server wich will contain the Evault
    # If you want use a Virtual Server instead a
    # Bare Metal server build a skeleton SoftLayer_Virtual_Guest object
    "virtualGuests": [
        {
            "complexType": "SoftLayer_Virtual_Guest",
            "id": 4241550
        }
    ],
    # The location for the Evault
    "location": "DALLAS06",
    "packageId": 0,
    # Build a skeleton SoftLayer_Product_Item_Price object.
    # The object contains the price ID of the Evaul device
    # you wish order.
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 1045
        }
    ],
    "quantity": 1
}

try:
    """
    # verifyOrder() will check your order for errors. Replace this with a call
    # to placeOrder() when you're ready to order. Both calls return a receipt
    # object that you can use for your records.
    #
    # Once your order is placed it'll go through SoftLayer's approval and
    # provisioning process.
    """
    result = productOrderService.verifyOrder(orderTemplate)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
