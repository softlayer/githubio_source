---
title: "Determining your next bill"
description: "Example on how to use getNextInvoiceTotalAmount to retrieve the pre-tax total amount of an account's next invoice measured in US Dollars ($USD)"
date: "2016-02-8"
classes: ["SoftLayer_Account"]
tags:
    - "invoice"
    - "billing"
---


```python

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
nextInvoiceAmount = client['SoftLayer_Account'].getNextInvoiceTotalAmount()
pp(nextInvoiceAmount)

```
