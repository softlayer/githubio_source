---
title: "get_credential_fortigate_firewall.rb"
description: "get_credential_fortigate_firewall.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan_Firewall"
tags:
    - "fotigatefirewall"
---


```
# Gets the credentials for a FortiGate Firewall
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan_Firewall
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan_Firewall/getManagementCredentials
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
APIKEY  = 'set me'
TIMEOUT = 120

# Declaring the API client to use the SoftLayer_Network_Vlan_Firewall API service
client = SoftLayer::Client.new(username: USERNAME, api_key: APIKEY, timeout: TIMEOUT)
network_vlan_firewall_service = client.service_named('SoftLayer_Network_Vlan_Firewall')

# The id of the fortigate firewall
fortigate_id = 4382

# Getting the credentials
credentials = network_vlan_firewall_service.object_with_id(fortigate_id).getManagementCredentials
print credentials

```
