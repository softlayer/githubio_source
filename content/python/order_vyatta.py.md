---
title: "order_vyatta.py"
description: "order_vyatta.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance"
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "viyatta"
---


```
"""
Order a Network Gateway Appliance (Vyatta)

The script orders a (Vyatta) high availability pair
it uses the SoftLayer_Product_Order::placeOrder to make the order
For more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

"""
Build a skeleton SoftLayer_Container_Product_Order object.
The object contains the configuration for the Vyatta server
such as the quantity, the location, etc.
"""
productOrder = {
    # The number of servers you wish to order.
    # If you wish a high availability pair you must specify 2 as quantity.
    "quantity": 2,
    # Build a skeleton SoftLayer_Hardware_Server object to model the hostname and
    # domain we want for our server. If you set quantity greater then 1 then you
    # need to define one hostname/domain pair per server you wish to order.
    "hardware": [
        {
            "hostname": "vyattagw",
            "domain": "test.com"
        },
        {
            "hostname": "vyattagw2",
            "domain": "test.com"
        }
    ],

    # Where you'd like your new server provisioned.
    # This can either be the id of the datacenter
    # you wish your new server to be provisioned in
    "location": 265592,
    # The id of the SoftLayer_Product_Package you wish to order.
    # In this case the Network Gateway Appliance (Vyatta) package id is 174.
    "packageId": 174,

    # Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
    # much more than ids, but SoftLayer's ordering system only needs the price's id
    # to know what you want to order.

    # Every item in SoftLayer's product catalog is assigned an id. Use these ids
    # to tell the SoftLayer API which options you want in your new server. Use
    # the getActivePackages() method in the SoftLayer_Account API service to get
    # a list of available item and price options per available package.
    "prices": [
        {"id": 13738},
        {"id": 21010},
        {"id": 36044},
        {"id": 876},
        {"id": 1267},
        {"id": 342},
        {"id": 273},
        {"id": 17129},
        {"id": 55},
        {"id": 58},
        {"id": 420},
        {"id": 418},
        {"id": 21},
        {"id": 57},
        {"id": 906}
        ]
    }

"""
Build a skeleton SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance object.
This object contains the order for the Vyatta server.
"""
orderData = {
    "orderContainers": [
        productOrder
    ]
}

# Create a SoftLayer API client object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
softLayerProductOrder = client["SoftLayer_Product_Order"]

try:
    """
    verifyOrder() will check your order for errors. Replace this with a call
    to placeOrder() when you're ready to order. Both calls return a receipt
    object that you can use for your records.

    Once your order is placed it'll go through SoftLayer's approval and
    provisioning process. When it's done you'll have a new
    SoftLayer_Hardware_Server object and server ready to use.
    """
    result = softLayerProductOrder.verifyOrder(orderData)
    print(result)
    print("The order was verified successfully")
except SoftLayer.SoftLayerAPIError as e:
    print("The order could not be verified by the server faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
