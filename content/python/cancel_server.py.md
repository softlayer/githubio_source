---
title: "cancel_server.py"
description: "cancel_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item_Hardware"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Cancel servers from a list of IPs

This script looks for a server with a determinated IP address and delete it.

It makes a single call to the cancelService() method in the
SoftLayer_Billing_Item API service

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Hardware
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The list of IPs from the servers you wish cancel
# (separate them by commas, e.g.: '10.48.66.132', '10.104.213.250')
ipsToCancel = ['10.48.66.132', '2.2.2.2']

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

"""
Declare a new API service objects for:
SoftLayer_Account
SoftLayer_Billing_Item
"""
accountClient = client['SoftLayer_Account']
billingItemClient = client['SoftLayer_Billing_Item']

"""
Add an object mask to retrieve our billing items related to the servers
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
for a list of the relational properties you can retrieve along with hardware.
"""
objectMask = 'mask[billingItem]'

# Make the call to retrieve our hardware records along with their billing item.
try:
    servers = accountClient.getHardware(mask=objectMask)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to list the bare metal servers. faultCode= %s, faultString= %s " % (e.faultCode, e.faultString))


# We are looking for the server which has the desired IP to delete it.
for ipToCancel in ipsToCancel:
    for server in servers:
        if 'primaryBackendIpAddress' in server.keys():
            if server['primaryBackendIpAddress'] == ipToCancel:
                if 'billingItem' in server.keys():
                    billingId = server['billingItem']['id']

                    try:
                        result = billingItemClient.cancelItem(id=billingId)
                        print(result)
                    except SoftLayer.SoftLayerAPIError as e:
                        """
                        If there was an error returned from the SoftLayer API then bomb out with the
                        error message.
                        """
                        print("Unable to cancel the server:  \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))

```
