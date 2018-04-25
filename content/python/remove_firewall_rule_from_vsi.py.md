---
title: "remove_firewall_rule_from_vsi.py"
description: "remove_firewall_rule_from_vsi.py"
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
Remove firewall rule from a  VSI.

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

ruleToDelete = {
    'action': 'permit',
    'protocol': 'tcp',
    'sourceIpAddress': '10.2.2.3',
    'destinationIpAddress': '169.57.129.196',
    'destinationPortRangeStart': 8084,
    'destinationPortRangeEnd': 8084,
}


client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
guestService = client['SoftLayer_Virtual_Guest']
firewallService = client['SoftLayer_Network_Component_Firewall']
firewallUpdateService = client['SoftLayer_Network_Firewall_Update_Request']

try:
    vsi = guestService.findByIpAddress(vsiIp)
    firewall = guestService.getFirewallServiceComponent(id=vsi['id'])
    oldRules = firewallService.getRules(id=firewall['id'])
    newRules = []
    for rule in oldRules:
        if rule['action'] == ruleToDelete['action'] and rule['protocol'] == ruleToDelete['protocol'] and rule['sourceIpAddress'] == ruleToDelete['sourceIpAddress'] and rule['destinationIpAddress'] == ruleToDelete['destinationIpAddress'] and rule['destinationPortRangeStart'] == ruleToDelete['destinationPortRangeStart'] and rule['destinationPortRangeEnd'] == ruleToDelete['destinationPortRangeEnd']:
            print("rule to delete: ")
            print(json.dumps(rule, sort_keys=True, indent=2, separators=(',', ': ')))
        else:
            newRules.append(rule)
    template = {
        'networkComponentFirewallId': firewall['id'],
        'rules': newRules
    }
    result = firewallUpdateService.createObject(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to remove the firewall rule. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
