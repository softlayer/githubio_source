---
title: "Create a Security group"
description: "Example for creating a Security Group."
date: "2017-06-20"
classes: 
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "objectTemplate"

---

## Creating a Security Group

```python
import SoftLayer
# For nice debug output:
from pprint import pprint as pp
# Create an object template to create the item.
objectTemplate = {
	'accountId': YOUR_ACCOUNT_ID,
    'name': 'pythonCreatedGroupExample',
    'description': 'Sec Group created via python'
} 
client = SoftLayer.Client()
try:
    result = client['SoftLayer_Network_SecurityGroup'].createObjects([objectTemplate])
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to create a new SecGroup  faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```

