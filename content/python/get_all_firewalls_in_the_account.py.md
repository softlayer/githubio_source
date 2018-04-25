---
title: "get_all_firewalls_in_the_account.py"
description: "get_all_firewalls_in_the_account.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "firewalls"
---


```
"""
Get the firewalls in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

vsiIp = "169.57.129.196"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[firewallNetworkComponents,networkVlanFirewall,dedicatedFirewallFlag,firewallGuestNetworkComponents,firewallInterfaces,firewallRules,highAvailabilityFirewallFlag]"

try:
    vlans = accountService.getNetworkVlans(mask=objectMask)
    firewalls = []
    for vlan in vlans:
        if vlan['dedicatedFirewallFlag'] == 1 or vlan['highAvailabilityFirewallFlag'] or len(vlan['firewallGuestNetworkComponents']) > 0 or len(vlan['firewallInterfaces']) > 0 or len(vlan['firewallNetworkComponents']):
            firewalls.append(vlan)
    print(json.dumps(firewalls, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the firewalls. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
