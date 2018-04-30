---
title: "update_anitvirus_spyware_policy.py"
description: "update_anitvirus_spyware_policy.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Software_Component_AntivirusSpyware"
tags:
    - "security"
---


```
"""
Updates the policy for a anti-virus or spyware.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_AntivirusSpyware
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_AntivirusSpyware/updateAntivirusSpywarePolicy

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

antivirusSpywareId = 2665230

# The valid values are:
# Minimal, Relaxed, Default, High, Ultimate
policy = "High"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
antivirusSpywareService = client['SoftLayer_Software_Component_AntivirusSpyware']

try:
    response = antivirusSpywareService.updateAntivirusSpywarePolicy(id=antivirusSpywareId)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to update the policy. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
