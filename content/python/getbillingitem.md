---
title: "Find a billing item from a provisioned product"
description: "Determine the billing item of a provisioned product using getBillingItem"
date: "2016-02-8"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectmask"
    - "billing"
---

In the following example we are looking for the Billing Item of an Virtual Guest with an ID of 1234567.

```python

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
mask = "mask[id]"
billingId = client['SoftLayer_Virtual_Guest'].getBillingItem(mask=mask,id=1234567)
pp(billingId)

```
