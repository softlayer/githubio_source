---
title: "get_vlans_for_order.py"
description: "get_vlans_for_order.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Location_Datacenter"
    - "SoftLayer_Product_Order"
tags:
    - "vlans"
---


```
"""
Get available VLANs for a new order

The script makes a single to call to SoftLayer_Product_Order::getVlans
method to call the available VLANs for the configuration of an order
for more details please see below.

Important manual pages:
https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/getVlans

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'


"""
The id for the datacenter where you are creating your machine
you can get the ids by using the "SoftLayer_Location_Datacenter" service
and the method "getDatacenters" e.g.
client = SoftLayer.Client(username=api_username,api_key=api_key)
datacenters = client['SoftLayer_Location_Datacenter'].getDatacenters()
"""
locationId = 265592

"""
The package id
you can get the list of packages ids by using the
SoftLayer_Product_Package service and the getAllObjects method e.g.
client = SoftLayer.Client(username=api_username,api_key=api_key)
packages = client['SoftLayer_Product_Package'].getAllObjects()
"""
packageId = 46

"""
The items that you selected in your order
on this case I am performing an order with the default values.
Also you can leave this parameter empty e.g.
selectedItems = ''
"""
selectedItems = 'guest_disk0=SAN_DISK,port_speed=100'

# Your account id
accountId = 307608

# Declaring a new API service object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Getting all available Vlans:
    vLans = client['SoftLayer_Product_Order'].getVlans(locationId, packageId, selectedItems, accountId)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to retrieve the VLANs. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))

print(vLans)

```
