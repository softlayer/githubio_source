---
title: "Cancel an item or service"
description: "Use cancelService to cancel an item or service
"
date: "2016-02-8"
classes: ["SoftLayer_Virtual_Guest", "SoftLayer_Billing_Item"]
tags:
    - "objectMask"
    - "billing"
---

In the following example we are retrieving the Billing Item of a Virtual Guest with the ID of 12345678 and passing that ID to [cancelService](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService).

```python

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
mask = "mask[id]"
billingId = client['SoftLayer_Virtual_Guest'].getBillingItem(mask=mask,id=12345678)
cancelItem = client['SoftLayer_Billing_Item'].cancelService(id = billingId['id'])

```
