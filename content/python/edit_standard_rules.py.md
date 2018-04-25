---
title: "edit_standard_rules.py"
description: "edit_standard_rules.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Network_Firewall_Update_Request"
    - "SoftLayer_Network_Component_Firewall_Update_Request_Rule"
tags:
    - "firewalls"
---


```
# Edit Standard Rule
# A rule set of a firewall is modified by passing a SoftLayer_Network_Firewall_Update_Request template object
# to SoftLayer_Network_Firewall_Update_Request::createObject. The entire rule set is rewritten with each
# update request. This means it is necessary to include all past unchanged rules along with any modifications
# or additions. This is easily accomplished by pulling in the existing rules as described above then modifying
# the gathered array.
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
import SoftLayer

# Your SoftLayer API username and key.
#
# Generate an API key at the SoftLayer Customer Portal
API_USERNAME = ''
API_KEY = 'apikey_goes_here'

# Create the client object
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

serverId = 5439388
objectMask = "mask[firewallServiceComponent[rules]]"
server = client['Virtual_Guest'].getObject(mask=objectMask, id=serverId)

try:
    # Modifying a rule
    if 'firewallServiceComponent' in server:
        ipToAllow = '192.168.1.1'
        index = 0
        if 'rules' in server['firewallServiceComponent']:
            rules = server['firewallServiceComponent']['rules']
            for rule in rules:
                if rule['sourceIpAddress'] == ipToAllow:
                    rule['action'] = 'deny'
                    rules[index] = rule
                index += 1
            updateRequestTemplate = {
                'firewallContextAccessControlListId': server['firewallServiceComponent']['id'],
                'rules': rules
            }
            updateRequestClient = client['SoftLayer_Network_Firewall_Update_Request'].createObject(
                updateRequestTemplate)
        print("Rule updated!")
    else:
        print("The server does not have firewall component")

except SoftLayer.SoftLayerAPIError as e:
    print("Error updating the rule  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
