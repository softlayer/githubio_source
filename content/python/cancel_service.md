---
title: "Cancel an item or service"
description: "Use cancelService to cancel an item or service
"
date: "2016-02-08"
classes: 
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Billing_Item_Hardware"
    - "SoftLayer_Billing_Item_Cancellation_Request"
tags:
    - "objectMask"
    - "billing"
---

This article will go over a variety of examples on how to cancel items on your account. Everything you order will have a corresponding SoftLayer_Billing_Item which is what specifically needs to be canceled. Some items, like Virtual_Guests have special cancel methods, but these are basically wrappers for canceling the billing item.


# Cancel Virtual Guest Service

In the following example we are retrieving the Billing Item of a Virtual Guest with the ID of 12345678 and passing that ID to [cancelService](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService).

```python
import SoftLayer

client = SoftLayer.Client()
mask = "mask[id]"
billingId = client['SoftLayer_Virtual_Guest'].getBillingItem(mask=mask,id=12345678)
cancelItem = client['SoftLayer_Billing_Item'].cancelService(id = billingId['id'])
```

If the billingId['id'] does not exist, this means the Virtual_Guest has already been canceled.

# Cancel server by private IP

```python
"""
Cancel servers from a list of IPs

This script looks for a server with a specific IP address and deletes it.
"""
import SoftLayer
client = SoftLayer.create_client_from_env()

# The list of IPs from the servers you wish cancel
ipsToCancel = ['10.48.66.132', '2.2.2.2']

"""
Declare these to keep line lengths minimal
"""
accountClient = client['SoftLayer_Account']
billingItemClient = client['SoftLayer_Billing_Item']

"""
Add an object mask to retrieve our billing items related to the servers
http://softlayer.github.io/reference/datatypes/SoftLayer_Hardware_Server
for a list of the relational properties you can retrieve along with hardware.
"""
objectMask = 'mask[billingItem]'

# Make the call to retrieve our hardware records along with their billing item.

# https://softlayer.github.io/reference/services/SoftLayer_Hardware_Server/findByIpAddress/ would also work. getHardware is useful for finding hardware based on other fields though.
servers = accountClient.getHardware(mask=objectMask)

# We are looking for the server which has the desired IP to delete it.
for server in servers:
    if 'primaryBackendIpAddress' in server.keys():
        if server['primaryBackendIpAddress'] in ipsToCancel:
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
print("Done")
```


# Cancel Load Balancer

```python
"""
Cancel load balancer.
"""

import SoftLayer
import json

# https://softlayer.github.io/reference/services/SoftLayer_Account/getLoadBalancers/ for finding loadBalancerIds
loadBalancerId = 109225
# False here will have the LB canceled at the billing anniversary date.
immediateCancellationFlag = True

client = SoftLayer.Client()
loadBalancerService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']
cancellationService = client['SoftLayer_Billing_Item_Cancellation_Request']

objectMask = "mask[accountId, dedicatedFlag, dedicatedBillingItem[id], billingItem[id]]"

try:
    loadBalancer = loadBalancerService.getObject(id=loadBalancerId, mask=objectMask)
    billingItemId = None
    if loadBalancer['dedicatedFlag']:
        billingItemId = loadBalancer['dedicatedBillingItem']['id']
    else:
        billingItemId = loadBalancer['billingItem']['id']
    cancelTemplate = {
        'accountId': loadBalancer['accountId'],
        'items': [
            {
                'billingItemId': billingItemId,
                'immediateCancellationFlag': immediateCancellationFlag
            }
        ]
    }
    result = cancellationService.createObject(cancelTemplate)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to cancel the load balancer. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```


# Cancel Global IP

```python
"""
Cancel Global IP address. Cancel the global IP address resource using its billing Item.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getGlobalIpRecord
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Use https://softlayer.github.io/reference/services/SoftLayer_Account/getGlobalIpRecords/ to find this Id.
globalIpId = 880617
mask = 'mask[id,billingItem[id]]'

client = SoftLayer.Client()


subnetResult = client['SoftLayer_Network_Subnet'].getGlobalIpRecord(id=globalIpId, mask=mask)
billingItemId = subnetResult['billingItem']['id']

try:
    client['SoftLayer_Billing_Item'].cancelItem(
        False,
        False,
        "No longer needed",
        "Api test",
        id=billingItemId)
except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to get billing item information faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```


# Cancel CDN Storage

```python
"""
Cancel CDN.
"""

import SoftLayer
import json

# The name of the CDN to cancel.
# https://softlayer.github.io/reference/services/SoftLayer_Account/getCdnAccounts/ Lists all CDN account names available
cdnAccountName = "14793"
immediateCancellation = True


client = SoftLayer.Client()
billingService = client['SoftLayer_Billing_Item_Cancellation_Request']
accountService = client['SoftLayer_Account']

# Set an object mask to get the billing item associated to the CDNN.
objectMask = "mask[billingItem]"

# Set an object filter to get only the configured CDN to delete in the result.
objectFilter = {"cdnAccounts": {"cdnAccountName": {"operation": cdnAccountName}}}

try:
    # Geting the CDN to delete
    cdns = accountService.getCdnAccounts(filter=objectFilter, mask=objectMask)
    if len(cdns) == 0:
        print ("The configured CDN: " + cdnAccountName + " does not exist in the account")
        exit(1)
    # Create the SoftLayer_Billing_Item_Cancellation_Request skeleton to create the cancellation request
    template = {
        "accountId": cdns[0]['accountId'],
        "items": [
            {
                "billingItemId": cdns[0]['billingItem']['id'],
                "immediateCancellationFlag": immediateCancellation
            }
        ]
    }
    result = billingService.createObject(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the cancel request"
          % (e.faultCode, e.faultString))
    exit(1)

```

# Cancel Storage Volume


```python
"""
Cancel Consistent Performance Storage iSCSI.
This script cancels the service of a Consistent Performance Storage iSCSI, passing a storage billing ID to
SoftLayer_Billing_Item::cancelService method.

"""
import SoftLayer
import pprint

"""
Set storage Id to Cancel, you can get a list of network storage available in the account
using the SoftLayer_Account::getNetworkStorage method.
"""
storageId = 4471311
# Use the mask to get billing item from a network storage
billingMask = 'mask[billingItem]'
# Create a client instance
client = SoftLayer.Client()
storage = client['SoftLayer_Network_Storage'].getObject(mask=billingMask, id=storageId)

billingId = storage['billingItem']['id']
try:
    result = client['SoftLayer_Billing_Item'].cancelService(id=billingId)
    print("Service cancelled")
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error cannot cancel the service  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```


# Cancel Subnet
Subnets should not have any hardware attached before they are canceled. Once a subnet is canceled, you can not get that specific subnet back. 


```python
"""
Cancel a Subnet. Cancel network subnet using its billing Item.
"""
import SoftLayer
from pprint import pprint as pp

# https://softlayer.github.io/reference/services/SoftLayer_Account/getSubnets/ To find subnet Ids
subnetId = 85467

client = SoftLayer.Client()


subnetResult = client['SoftLayer_Network_Subnet'].getBillingItem(id=subnetId)
billingItemId = subnetResult['id']

try:
    result = client['SoftLayer_Billing_Item'].cancelItem(
        False,
        False,
        "No longer needed",
        "Api test",
        id=billingItemId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Unable to get billing item information faultCode=%s, faultString=%s'
        % (e.faultCode, e.faultString))

```


# Cancel VLAN
Vlans do need to be empty to be canceled. 

```python
"""
Example to cancel a VLAN

The script will get the Billing_Item id of the VLAN service then it will cancel the VLAN service
"""
import SoftLayer.API
from pprint import pprint as pp

# The VLAN id you wish to cancel
# https://softlayer.github.io/reference/services/SoftLayer_Account/getNetworkVlans/ to get vlan ids
vlanId = 563298

# Declare the API client
client = SoftLayer.Client()
networkVlanService = client['SoftLayer_Network_Vlan']
billingItemService = client['SoftLayer_Billing_Item']

# Declaring an object mask to get the billing item information
objectMask = 'mask[billingItem]'

try:
    # Getting the Billing Item to cancel the VLAN service.
    vlan = networkVlanService.getObject(mask=objectMask, id=vlanId)
    pp(vlan)
    # Canceling the VLAN service.
    result = billingItemService.cancelService(id=vlan['billingItem']['id'])
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to cancel the VLAN. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```