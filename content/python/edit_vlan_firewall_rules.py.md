---
title: "edit_vlan_firewall_rules.py"
description: "edit_vlan_firewall_rules.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Network_Firewall_Update_Request"
    - "SoftLayer_Network_Component_Firewall_Update_Request_Rule"
    - "SoftLayer_Network_Vlan"
tags:
    - "firewalls"
---


```
# Edit Vlan firewall rule.
#
# A firewall's ruleset is modified by passing a SoftLayer_Network_Firewall_Update_Request template
# object to SoftLayer_Network_Firewall_Update_Request::createObject. The entire ruleset is rewritten
# with each update request. This means it is necessary to include all past unchanged rules along with any
# modifications or additions. This is easily accomplished by pulling in the existing rules as described above
# then modifying the gathered array.
# Each SoftLayer_Network_Component_Firewall_Update_Request_Rule object requires:
#
# action - permit or deny
# destinationIpAddress - destination address
# destinationIpSubnetMask - subnet mask for destination
# sourceIpAddress - originating address
# sourceIpSubnetMask - subnet mask for origin address
# protocol - tcp/udp
# destinationPortRangeStart - first port the rule will effect
# destinationPortRangeEnd - last port the rule will effect
# orderValue - order in which rules are applied (lower is sooner)
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Firewall_Update_Request
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Firewall_Update_Request/createObject
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

# So we can talk to the SoftLayer API:
import SoftLayer.API

# For nice debug output:
import pprint

# Your SoftLayer API username and key.
#
# Generate an API key at the SoftLayer Customer Portal

API_USERNAME = ''
API_KEY = 'apikey_goes_here'

vlanId = 211163
# Create the client object
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
objectMask = 'mask[firewallRules,firewallInterfaces[firewallContextAccessControlLists]]'
vlan = client['SoftLayer_Network_Vlan'].getObject(mask=objectMask, id=vlanId)
rules = vlan['firewallRules']

firewallContextAccessControlListId = ''
# Getting the ID of Access Control List.
# Each VLAN will have two types of firewallInterface: 'inside' and 'outside'.
# firewallContextAccessControlLists are organized by a direction of 'in' or 'out'.
# Currently the SoftLayer Platform supports the 'outside' firewallInterfaces
for firewall in vlan['firewallInterfaces']:
    if firewall['name'] == 'inside':
        continue
    for controlList in firewall['firewallContextAccessControlLists']:
        if controlList['direction'] == 'out':
            continue
        firewallContextAccessControlListId = controlList['id']
try:
    # Modifying a rule
    ipToAllow = '119.81.91.198 '
    index = 0
    for rule in rules:
        if rule['sourceIpAddress'] == ipToAllow:
            rule['action'] = 'permit'
            rules[index] = rule
        index += 1
    updateRequestTemplate = {
        'firewallContextAccessControlListId': firewallContextAccessControlListId,
        'rules': rules
    }
    updateRequestClient = client['SoftLayer_Network_Firewall_Update_Request'].createObject(updateRequestTemplate)
    pprint.pprint('Rule updated!')

except SoftLayer.SoftLayerAPIError as e:
    print("Error updating the rule  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
