---
title: "Get verbose details about a Bare Metal Server"
description: "Retrieve the packages, categories and items associated with a Bare Metal Server."
date: "2016-12-29"
classes: ["SoftLayer_Hardware"]
tags:
    - "objectmask"
    - "getobject"
---

This script will get the Packages, Categories, and items associated with a Bare Metal Server. 

```python

import SoftLayer
import pprint
from pprint import pprint as pp

client = SoftLayer.Client()

mask = "mask[id, fullyQualifiedDomainName, billingItem[id, item[id, description], category[name, id],children[id, item[id, description], category[name, id]]]]"

getDetails = client['SoftLayer_Hardware'].getObject(mask=mask,id=296740)
pp(getDetails)

```