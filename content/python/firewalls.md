---
title: "Working with Firewalls"
description: "A few examples on interacting with Firewalls"
date: "2022-01-05"
classes:
- "SoftLayer_Account"
- "SoftLayer_Virtual_Guest"
- "SoftLayer_Network_Vlan"
- "SoftLayer_Network_Vlan_Firewall"
- "SoftLayer_Network_Component_Firewall"
- "SoftLayer_Network_Firewall_Update_Request"
- "SoftLayer_Network_Subnet_IpAddress"
- "SoftLayer_Network_Firewall_Update_Request_Rule"
tags:
- "firewalls"
---

### Setup
All the functions defined in this article will be part of this `FirewallExample` class. Which only sets up the SoftLayer Client, and configures the debugger, which allows you to see the exact API calls being made.

```python
from pprint import pprint

import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import formatting
import json


class FirewallExample:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger
        self.env = environment.Environment()

    def debug(self):
        for call in self.client.transport.get_last_calls():
            pprint(self.client.transport.print_reproduceable(call))

```

## Get a Firewall for a Vsi
To get the firewall associated to a VSI.

### Python
```python

    def get_firewall_for_a_vsi(self, primary_ip_address):
        vsi = self.client.call('SoftLayer_Virtual_Guest', 'findByIpAddress', primary_ip_address)
        firewall = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallServiceComponent', id=vsi['id'])
        self.env.fout(formatting.iter_to_table(firewall))

```

## Backup and Restore Firewall Rules
A quick example on how to backup firewall rules to a file and restore those rules so for this section needs the firewall id and obtains in this function `get_firewall_for_a_vsi()`.

RestoreRules here will clobber any existing rules on the firewall, so be careful with that.

### Python
```python

    def backup_firewall_rules(self, path, id_firewall):
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=id_firewall)
        with open(path, 'w') as f:
            json.dump(rules, f)
        print("Done saving rules to %s" % path)

    def restore_firewall_rules(self, path, id_firewall):
        with open(path, 'r') as f:
            rules = json.load(f)
        
        for rule in rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']

        rules_template = {
            'networkComponentFirewallId': id_firewall,
            'rules': rules
        }
        result = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(result))
```

## Remove Firewall Rule from Vsi
Remove firewall rule from a VSI. For remove any rule, it's necessary obtain the id of the rule, this it's possible with the follow function `get_firewall_rules`. 
### Python
```python

    def get_firewall_rules(self, id_firewall):
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=id_firewall)
        self.env.fout(formatting.iter_to_table(rules))

    def remove_firewall_rule_from_vsi(self, id_firewall, id_rule):
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=id_firewall)

        for rule in rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']
            if rule['id'] == id_rule:
                # This rule will be deleted
                rules.remove(rule)

        rules_template = {
            'networkComponentFirewallId': id_firewall,
            'rules': rules
        }
        new_rules = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(new_rules))


```

## Process Rules for a Firewall in a Bypass
Process rules for a firewall in a VSI.
### Python
```python

    def process_rules_for_a_firewall_in_a_bypass(self, id_firewall):
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=id_firewall)

        for rule in rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']

        rules_template = {
            'bypassFlag': False,
            'networkComponentFirewallId': id_firewall,
            'rules': rules
        }
        new_rules = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(new_rules))

```
## Bypass Rules for a Firewall in a Bypass
Bypass rules for a firewall in a VSI.
### Python
```python

    def bypass_rules_for_a_firewall_in_a_bypass(self, id_firewall):
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=id_firewall)

        for rule in rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']

        rules_template = {
            'bypassFlag': True,
            'networkComponentFirewallId': id_firewall,
            'rules': rules
        }
        new_rules = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(new_rules))

```

## Get Firewall Rules for a Vsi
Get the associated Firewall's rules for a vsi.
### Python
```python

    def get_rules_for_a_vsi(self, primary_ip_address):
        vsi = self.client.call('SoftLayer_Virtual_Guest', 'findByIpAddress', primary_ip_address)
        firewall = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallServiceComponent', id=vsi['id'])
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=firewall['id'])
        self.env.fout(formatting.iter_to_table(rules))

```

## Get Firewall Logs
Get the firewall logs for an arbitrary IP address.
### Python
```python

    def get_firewall_logs(self, primary_ip_address):
        subnetIp = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getByIpAddress', primary_ip_address)
        self.env.fout(formatting.iter_to_table(subnetIp))
        logs = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getSyslogEventsOneDay', id=subnetIp['id'], limit=10)
        self.env.fout(formatting.iter_to_table(logs))

```

## Get Firewall Ip Address
Get the IP address from a VLan.

The script lists the IP address of VLAN, it makes a single call to the `SoftLayer_Network_Vlan::getFirewallProtectableIpAddresses` method.

### Python
```python

    def get_firewall_ip_address(self, primary_ip_address):
        vlan = self.client.call('SoftLayer_Network_Vlan', 'getVlanForIpAddress', primary_ip_address)
        self.env.fout(formatting.iter_to_table(vlan))
        firewall = self.client.call('SoftLayer_Network_Vlan', 'getFirewallProtectableIpAddresses', id=vlan['id'], limit=10)
        self.env.fout(formatting.iter_to_table(firewall))

```

## Edit Standard Rules
Edit Standard Rule`.

A rule set of a firewall is modified by passing a SoftLayer_Network_Firewall_Update_Request template object to SoftLayer_Network_Firewall_Update_Request::createObject. The entire rule set is rewritten with each update request.

This means it is necessary to include all past unchanged rules along with any modifications or additions. This is easily accomplished by pulling in the existing rules as described above then modifying the gathered array.

### Python
```python

    def edit_standard_rules(self, id_server, ip_to_allow):
        firewall = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallServiceComponent', id=id_server)
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=firewall['id'])

        for rule in rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']
            if rule['sourceIpAddress'] == ip_to_allow:
                rule['action'] = 'deny'

        rules_template = {
            'networkComponentFirewallId': id_firewall,
            'rules': rules
        }
        new_rules = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(new_rules))

```

## Edit Firewall Rule from Vsi
Edit a firewall rule from a  VSI.
For edit any rule, it's necessary obtain the id of the rule, this it's possible with the follow function `get_firewall_rules`.

### Python
```python

    def edit_firewall_rule_from_vsi(self, primary_ip_address, id_rule, new_rule):
        vsi = self.client.call('SoftLayer_Virtual_Guest', 'findByIpAddress', primary_ip_address)
        firewall = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallServiceComponent', id=vsi['id'])
        rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=firewall['id'])

        for index in range(len(rules)):
            # It is always necessary to delete this key to perform the firewall update request
            del rules[index]['status']
            if rules[index]['id'] == id_rule:
                rules[index] = new_rule

        rules_template = {
            'networkComponentFirewallId': id_firewall,
            'rules': rules
        }
        new_rules = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(new_rules))

```

## Firewall Report
Get firewall report.

### Python
```python

    def firewall_report(self, ip_address_id):
        logs = self.client.call('SoftLayer_Network_Subnet_IpAddress', 'getTopTenSyslogEventsByProtocolsOneDay', id=ip_address_id)
        self.env.fout(formatting.iter_to_table(logs))

```

## Get All Firewalls in the Account
Get the firewalls in the account.

### Python
```python

    def get_all_firewalls_in_the_account(self):
        objectMask = "mask[firewallNetworkComponents,networkVlanFirewall,dedicatedFirewallFlag,firewallGuestNetworkComponents,firewallInterfaces,firewallRules,highAvailabilityFirewallFlag]"
        vlans = self.client.call('SoftLayer_Account', 'getNetworkVlans', mask=objectMask)

        firewalls = []
        for vlan in vlans:
            if vlan['dedicatedFirewallFlag'] == 1 or vlan['highAvailabilityFirewallFlag'] or len(
                    vlan['firewallGuestNetworkComponents']) > 0 or len(vlan['firewallInterfaces']) > 0 or len(
                vlan['firewallNetworkComponents']):
                firewalls.append(vlan)

        self.env.fout(formatting.iter_to_table(firewalls))

```

## Get All Firewalls in the Account
Get the firewalls in the account.

### Python
```python

    def get_all_firewalls_in_the_account(self):
        objectMask = "mask[firewallNetworkComponents,networkVlanFirewall,dedicatedFirewallFlag,firewallGuestNetworkComponents,firewallInterfaces,firewallRules,highAvailabilityFirewallFlag]"
        vlans = self.client.call('SoftLayer_Account', 'getNetworkVlans', mask=objectMask)

        firewalls = []
        for vlan in vlans:
            if vlan['dedicatedFirewallFlag'] == 1 or vlan['highAvailabilityFirewallFlag'] or len(
                    vlan['firewallGuestNetworkComponents']) > 0 or len(vlan['firewallInterfaces']) > 0 or len(
                vlan['firewallNetworkComponents']):
                firewalls.append(vlan)

        self.env.fout(formatting.iter_to_table(firewalls))

```

## Add Firewall Rule to Vsi
Add firewall rules to the Firewall in a VSI.

### Python
```python

    def add_firewall_rule_to_vsi(self, primary_ip_address, rules):
        vsi = self.client.call('SoftLayer_Virtual_Guest', 'findByIpAddress', primary_ip_address)
        firewall = self.client.call('SoftLayer_Virtual_Guest', 'getFirewallServiceComponent', id=vsi['id'])
        old_rules = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=firewall['id'])

        for rule in old_rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']

        new_rules = old_rules + rules

        rules_template = {
            'networkComponentFirewallId': id_firewall,
            'rules': new_rules
        }
        result = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(result))

```

## Edit Vlan Firewall Rules
Edit Vlan firewall rule.

A firewall's ruleset is modified by passing a SoftLayer_Network_Firewall_Update_Request template object to `SoftLayer_Network_Firewall_Update_Request::createObject`. The entire ruleset is rewritten with each update request.

This means it is necessary to include all past unchanged rules along with any modifications or additions. This is easily accomplished by pulling in the existing rules as described above then modifying the gathered array.

### Python
```python

    def edit_vlan_firewall_rules(self, vlan_id, ip_to_allow):
        objectMask = 'mask[firewallRules,firewallInterfaces[firewallContextAccessControlLists]]'
        vlan = self.client.call('SoftLayer_Network_Vlan', 'getObject', id=vlan_id, mask=objectMask)
        rules = vlan['firewallRules']
        self.env.fout(formatting.iter_to_table(rules))

        firewallContextAccessControlListId = ''
        # Getting the ID of Access Control List.
        # Each VLAN will have two types of firewallInterface: 'inside' and 'outside'.
        # firewallContextAccessControlLists are organized by a direction of 'in' or 'out'.
        # Currently the SoftLayer Platform supports the 'outside' firewallInterfaces`.

        for firewall in vlan['firewallInterfaces']:
            if firewall['name'] == 'inside':
                continue
            for controlList in firewall['firewallContextAccessControlLists']:
                if controlList['direction'] == 'out':
                    continue
                firewallContextAccessControlListId = controlList['id']

        for rule in rules:
            # It is always necessary to delete this key to perform the firewall update request
            del rule['status']
            if rule['sourceIpAddress'] == ip_to_allow:
                rule['action'] = 'permit'

        rules_template = {
            'firewallContextAccessControlListId': firewallContextAccessControlListId,
            'rules': rules
        }

        result = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', rules_template)
        self.env.fout(formatting.iter_to_table(result))

```

## Running the Example

### Python
```python

if __name__ == '__main__':
    firewall = FirewallExample()
    primary_ip_address = '0.0.0.0'
    firewall.get_firewall_for_a_vsi(primary_ip_address)

    path = '/yourPath'
    id_firewall = 123456
    firewall.backup_firewall_rules(path, id_firewall)
    firewall.restore_firewall_rules(path, id_firewall)

    # For remove any rule, it's necessary obtain the id of the rule, this it's possible with the follow function:
    firewall.get_firewall_rules(id_firewall)

    id_rule = 1234567
    firewall.remove_firewall_rule_from_vsi(id_firewall, id_rule)

    firewall.process_rules_for_a_firewall_in_a_bypass(id_firewall)

    firewall.bypass_rules_for_a_firewall_in_a_bypass(id_firewall)

    firewall.get_rules_for_a_vsi(primary_ip_address)

    firewall.get_firewall_logs(primary_ip_address)

    firewall.get_firewall_ip_address(primary_ip_address)

    id_server = 123456789
    ip_to_allow = '0.0.0.0'
    firewall.edit_standard_rules(id_server, ip_to_allow)

    new_rule = {
        "action": "permit",
        "destinationIpAddress": "any on server",
        "destinationPortRangeEnd": 80,
        "destinationPortRangeStart": 80,
        "orderValue": 1,
        "protocol": "tcp",
        "sourceIpAddress": "0.0.0.0",
        "sourceIpSubnetMask": "0.0.0.0"
    }
    firewall.edit_firewall_rule_from_vsi(primary_ip_address, id_rule, new_rule)

    ip_address_id = 123456789
    firewall.firewall_report(ip_address_id)

    firewall.get_all_firewalls_in_the_account()

    new_rules = [{
        "action": "permit",
        "destinationIpAddress": "any on server",
        "destinationPortRangeEnd": 22,
        "destinationPortRangeStart": 22,
        "orderValue": 1,
        "protocol": "tcp",
        "sourceIpAddress": "0.0.0.0",
        "sourceIpSubnetMask": "0.0.0.0"
    }]
    firewall.add_firewall_rule_to_vsi(primary_ip_address, new_rules)
    
    vlan_id = 1234567
    firewall.edit_vlan_firewall_rules(vlan_id, ip_to_allow)
    firewall.debug()


```

If you want to know the VSI of your account or require any additional information, you can start with the following documentation, which offers you the required data `SoftLayer_Account::getVirtualGuests`.
