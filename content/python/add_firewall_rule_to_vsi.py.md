---
title: "add_firewall_rule_to_vsi.py"
description: "add_firewall_rule_to_vsi.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Firewall_Update_Request"
    - "SoftLayer_Network_Component_Firewall"
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
tags:
    - "firewalls"
---


```
"""
Add firewall rules to the Firewall in a VSI.

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

# Creating an array SoftLayer_Network_Firewall_Update_Request_Rule skeleton object
# which contains the rules to add to the firewall.
rules = [
    {
        'action': 'permit',
        'protocol': 'tcp',
        'version': 4,
        'sourceIpAddress': '10.2.2.3',
        'orderValue': 5,
        'sourceIpCidr': 32,
        'destinationIpAddress': '169.57.129.196',
        'destinationIpCidr': 32,
        'destinationPortRangeStart': 8084,
        'destinationPortRangeEnd': 8084,
        'notes': 'this is my note',
        'ruleAction': 'permit'
    },
    {
        'action': 'permit',
        'protocol': 'tcp',
        'version': 6,
        'sourceIpAddress': 'FE80::0202:B3FF:FE1E:8329',
        'orderValue': 3,
        'sourceIpCidr': 128,
        'destinationIpAddress': 'any',
        'destinationIpCidr': 128,
        'destinationPortRangeStart': 4130,
        'destinationPortRangeEnd': 4130,
        'notes': 'this is my note',
        'ruleAction': 'permit'
    }
]


client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
guestService = client['SoftLayer_Virtual_Guest']
firewallService = client['SoftLayer_Network_Component_Firewall']
firewallUpdateService = client['SoftLayer_Network_Firewall_Update_Request']

try:
    vsi = guestService.findByIpAddress(vsiIp)
    firewall = guestService.getFirewallServiceComponent(id=vsi['id'])
    oldRules = firewallService.getRules(id=firewall['id'])
    newRules = oldRules + rules    
    template = {
        'networkComponentFirewallId': firewall['id'],
        'rules': newRules
    }
    result = firewallUpdateService.createObject(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to add the firewall rule. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
