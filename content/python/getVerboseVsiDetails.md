---
title: "Get verbose details about a Virtual Guest"
description: "Retrieve the packages, categories and items associated with a Virtual Guest."
date: "2016-12-29"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
---

This script will get the Packages, Categories, and items associated with a Virtual Guest. 

```python

import SoftLayer
import pprint
from pprint import pprint as pp

client = SoftLayer.Client()

mask = "mask[id, fullyQualifiedDomainName, billingItem[id, item[id, description], category[name, id],children[id, item[id, description], category[name, id]]]]"

getDetails = client['SoftLayer_Virtual_Guest'].getObject(mask=mask,id=26961063)
pp(getDetails)

```