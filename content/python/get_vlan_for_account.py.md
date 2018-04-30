---
title: "get_vlan_for_account.py"
description: "get_vlan_for_account.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "vlans"
---


```
"""
Example to get the VLANS in an account

The example retrieves a list of all VLANs in the account.
It makes a single call to the SoftLayer_Account::getPublicNetworkVlans
method. For more information please see below.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPublicNetworkVlans
http://sldn.softlayer.com/reference/services/SoftLayer_Account/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

# Declaring an object mask to get more information about the VLANs
objectMask = "primaryRouter[datacenter], dedicatedFirewallFlag, firewallNetworkComponentCount, firewallGuestNetworkComponentCount, firewallInterfaces, highAvailabilityFirewallFlag, networkVlanFirewall"

try:
    # Getting the VLANs
    result = client['SoftLayer_Account'].getPublicNetworkVlans(mask=objectMask)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to get Vlans. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))

```
