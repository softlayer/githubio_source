---
title: "place_quote_order.py"
description: "place_quote_order.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---


```
"""
Order from account's quote.
This script creates an order from a account's quote presented
in the SoftLayer Customer Portal's (https://control.softlayer.com/account/quotes)

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getQuotes
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getRecalculatedOrderContainer
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/placeOrder
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice debug output:
import pprint
"""
Your SoftLayer API username and key.
Generate an API key at the SoftLayer Customer Portal
"""
API_USERNAME = 'set-me'
API_KEY = 'set-me'
"""
Set the id of the quote from which you want to create the order,
use SoftLayer_Account::getQuotes method to get a list of quotes from account
"""
quoteId = 1186525
# Get the order data by using SoftLayer_Billing_Order_Quote::getRecalculatedOrderContainer method
orderTemplates = client['SoftLayer_Billing_Order_Quote'].getRecalculatedOrderContainer(id=quoteId)
"""
For this example we are retrieving the data from a quote which
contains configuration to order a single server.
"""

orderData = orderTemplates['orderContainers'][0]

"""
Set template information for the new order.
First, declare the template as a
SoftLayer_Container_Product_Order_Hardware_Server type, so the API knows
you're trying to place an order for a server.
orderData['complexType'] = 'SoftLayer_Container_Product_Order_Hardware_Server'
We want to order one server.
"""
orderData['quantity'] = 1

# Location
orderData['location'] = '154820'

# Set the preset Id
orderData['presetId'] = None
"""
Set the hostname and domain for our new server. If ordering more
than one server then define another hostname/domain pair accordingly.
"""
orderData['hardware'] = [{'hostname': 'server01', 'domain': 'example.com'}]
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
try:
    """
    Verify the order container is right. If this returns an error
    then fix your order container and re-submit. Once ready then place
    your order with the placeOrder() method.
    """
    receipt = client['SoftLayer_Billing_Order_Quote'].verifyOrder(orderData, id=quoteId)
    pprint.pprint(receipt)
except SoftLayer.SoftLayerAPIError as e:
    print("error faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
