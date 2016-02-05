---
title: "Month-to-date cost of a Virtual_Guest"
description: "Determine the month-to-date cost of an hourly Virtual_Guest using getBillingItem and an objectMask"
date: "2016-02-8"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "billing"
---


```python

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
mask = "mask[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge]"
toDateCost = client['SoftLayer_Virtual_Guest'].getBillingItem(mask=mask,id=1234567)
pp(toDateCost)

```

Example Response

```json

{'createDate': '2016-02-05T14:07:37-06:00',
  'currentHourlyCharge': '.023',
  'hourlyRecurringFee': '.023',
  'hoursUsed': '1'}

```
