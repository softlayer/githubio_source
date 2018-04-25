---
title: "list_subnets.py"
description: "list_subnets.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "subnets"
---


```
"""
List subnets. It retrieves all network subnets associated with an account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnets
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    result = client['SoftLayer_Account'].getSubnets()
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the subnets faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
