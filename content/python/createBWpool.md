---
title: "Create a new Bandwidth Pool"
description: "Creating a new Bandwidth pool. This allows you to optimize your bandwidth usage by "pooling" all of the bandwidth together for servers in a the Pool."
date: "2016-04-29"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "BandwidthPool"
    - "createObject"
---

```python

import SoftLayer
# For nice debug output:
from pprint import pprint as pp


# Set the needed values to create a new item
accountId = 111111

# The values for bandwidthAllotmentTypeId are: (1) and (2)
# where: (1) means this allotment is marked as a virtual private rack or
#        (2) bandwidth pooling
bandwidthAllotmentTypeId = 2

# To get locationGroupId, execute: SoftLayer_Location_Group::getAllObjects
locationGroupId = 1
newBandwithPoolName = 'newBWpool'

# Create an object template to create the item.
objectTemplate = {
    'accountId': accountId,
    'bandwidthAllotmentTypeId': bandwidthAllotmentTypeId,
    'locationGroupId': locationGroupId,
    'name': newBandwithPoolName
}

# Creates a new connection to the API service.
client = SoftLayer.Client()

try:
    result = client['SoftLayer_Network_Bandwidth_Version1_Allotment'].createObject(objectTemplate)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to create a new Bandwidth Pool  faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))
```
