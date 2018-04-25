---
title: "update_hostids.py"
description: "update_hostids.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Software_Component_HostIps"
tags:
    - "security"
---


```
"""
Update Host IDS policy.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_HostIps
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_HostIps/updateHipsPolicies

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The hostidsid you wish to update the policy.
hostidsId = 6114923

# Values
# __EPO_ENFORCE_YES__
# __EPO_ENFORCE_NO__
newEnforcementPolicy = "__EPO_ENFORCE_NO__"

# Values
# McAfee Default
# My Default
# On_120
# On [McAfee Default]
# Adaptive_10
# Adaptive_120
# Adaptive_UR
# On_10
# On_UR
# Off
newIpsMode = "On_120"

# Values
# Basic Protection [McAfee Default]
# Enhanced Protection
# Maximum Protection
# Prepare for Enhanced Protection
# Prepare for Maximum Protection
# Warning
# My Default
newIpsProtection = "Basic Protection [McAfee Default]"

# Values
# McAfee Default
# My Default
# Off [McAfee Default]
# On
# Adaptive
# Learn
# Custom_FWONSpecial_DONOTUSE
newFirewallMode = "Off [McAfee Default]"

# Values
# McAfee Default
# Typical Corporate Environment
# SLDefault
# No_Rules
# My Default
newFirewallRuleset = "SLDefault"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
hostidsService = client['SoftLayer_Software_Component_HostIps']

try:
    response = hostidsService.updateHipsPolicies(newIpsMode, newIpsProtection, newFirewallMode, newFirewallRuleset, "", "", newEnforcementPolicy, id=hostidsId)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to update the policy. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
