---
title: "Place quote order"
description: "Retrieve an order object from a quote and place an order based on it"
date: "2014-02-12"
classes: ["SoftLayer_User_Customer","SoftLayer_Account"]
tags:
    - "order"
    - "quote"
---


```python
import SoftLayer
from pprint import pprint as pp
 
quote_id = 12345
client = SoftLayer.Client()

def getOrderContainer(quote_id):
    container = client['Billing_Order_Quote'].getRecalculatedOrderContainer(id=quote_id)
    return container['orderContainers'][0]
 
def getQuotes():
    quotes = client['SoftLayer_Account'].getQuotes()
    pp(quotes)

getQuotes()
container = getOrderContainer(quote_id)
order = {}
order['complexType'] = 'Container_Product_Order_Virtual_Guest'
order['hardware'] = [{'hostname': 'quotetest', 'domain': 'example.com'}]
order['quanity'] = 1
result = client['Billing_Order_Quote'].verifyOrder(order, id=quote_id)

pp(result)

```
