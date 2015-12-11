---
title: "Set a server's metadata"
description: "Set a server's metadata"
date: "2015-03-23"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "server"
    - "metadata"
---

```python
import SoftLayer
from pprint import pprint as pp

# CHANGE ME
server = 678243 

client = SoftLayer.Client()

mask = "mask[attributes]"

# Sets the metadata for this server to tttttt
result1 = client['SoftLayer_Hardware_Server'].setUserMetadata({'value': 'tttttt'},id=server)
pp(result1)

result2 = client['SoftLayer_Hardware_Server'].getObject(mask=mask,id=server)

pp(result2)
```
