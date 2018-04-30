---
title: "order_dedicated_firewall.py"
description: "order_dedicated_firewall.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "firewalls"
---


```
"""
Order dedicated firewall

The script calls the SoftLayer_Product_Order::placeOrder method to
order a firewall.
for more information see below.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
"""
import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# Build a skeleton SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated object
# containing the order you wish to place.
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Protection_Firewall",
    "virtualGuests": [
        {
            "complexType": "SoftLayer_Virtual_Guest",
            "id": 6674100  # the virtual Guest ID where you wish add a firewall.
        }
    ],
    "location": 168642,  # the location for the firewall in this case "San Jose 1"
    "packageId": 0,  # the package id to order firewalls
    # The prices to order the firewall
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 410  # price to 10Mbps Hardware Firewall
        }
    ],
    "quantity": 1,  # we only want 1 firewall
}

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
