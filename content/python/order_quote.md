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
    quotes = client['SoftLayer_Account'].getActiveQuotes()
    pp(quotes)

getQuotes()
guests = {'hostname': 'quotetest', 'domain': 'example.com'}
container = getOrderContainer(quote_id)
container['quantity'] = 1
container['virtualGuests'] = []
# You will need to add a hostname and domain entry for each server on the order
# if quantity was 5, you would need to add 5 guests here
container['virtualGuests'].append(guests)
container['presetId'] = None
result = client['Product_Order'].verifyOrder(container)

pp(result)

```
