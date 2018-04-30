---
title: "bypass_rules_for_a_firewall_in_a_bypass.py"
description: "bypass_rules_for_a_firewall_in_a_bypass.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Firewall_Update_Request"
    - "SoftLayer_Network_Component_Firewall"
tags:
    - "firewalls"
---


```
"""
Bypass rules for a firewall in a VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Firewall_Update_Request/createObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

vsiIp = "169.57.129.196"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
guestService = client['SoftLayer_Virtual_Guest']
firewallService = client['SoftLayer_Network_Component_Firewall']
firewallUpdateService = client['SoftLayer_Network_Firewall_Update_Request']

try:
    vsi = guestService.findByIpAddress(vsiIp)
    firewall = guestService.getFirewallServiceComponent(id=vsi['id'])
    oldRules = firewallService.getRules(id=firewall['id'])
    template = {
        'bypassFlag': True,
        'networkComponentFirewallId': firewall['id'],
        'rules': oldRules
    }
    result = firewallUpdateService.createObject(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to bypass the rules. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
