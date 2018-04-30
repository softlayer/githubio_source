---
title: "order_subnet.py"
description: "order_subnet.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
---


```
"""
Order a new subnet.

The script order a new subnet using the same options like the portal.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getAllObjects
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getSubnetForIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet
http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-3
http://sldn.softlayer.com/article/Object-Filters
http://sldn.softlayer.com/article/Python
http://sldn.softlayer.com/article/Object-Masks


License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# The subnet you wish to order. The available options are the
# same like in the in the Softlayer Portal.
# e.g. "1 Static Public IP Address",
# "/64 Block Static Public IPv6 Addresses", etc.
option = "Global IPv6"

# The endpoint IP address for the subnet.
# You need to configure this field if
# your order belongs to the categories
# "Static Public" or "Static Public IPv6"
# e.g. "119.81.142.114", "2401:c900:1201:9c::2".
endPointIP = "119.81.142.114"

# The VLan number for the subnet.
# You need to configure this field if
# your order belongs to the categories
# "Portable Public", "Portable Private" and
# "Portable Public IPv6".
vlanNumber = 758

client = SoftLayer.Client()
packageService = client['SoftLayer_Product_Package']
subnetService = client['SoftLayer_Network_Subnet']
orderService = client['SoftLayer_Product_Order']
accountService = client['SoftLayer_Account']

# Declaring an object filter to get the packages
# related to subnets.
objectFilter = {
    "type": {
        "keyName": {
            "operation": "in",
            "options": [{
                "name": "data",
                "value": [
                    "ADDITIONAL_SERVICES",
                    "ADDITIONAL_SERVICES_PORTABLE_IP_ADDRESSES",
                    "ADDITIONAL_SERVICES_STATIC_IP_ADDRESSES"
                ]
            }]
        }
    }
}

# Declaring an object mask to get more information about the packages
objectMask = "mask[items[id, description, prices[id, recurringFee, attributes, categories]]]"

# Getting the items and the prices available to order subnets
try:
    packages = packageService.getAllObjects(filter=objectFilter,
                                            mask=objectMask)

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the packages. faultCode=%s, faultString=%s" %
          (e.faultCode, e.faultString))
    exit(1)

# Getting item price for the configured option to order.
optionItem = {}
optionPackage = 0
for package in packages:
    for item in package['items']:
        if item['description'] == option:
            prices = []
            if len(item['prices']) > 1:
                for price in item['prices']:
                    if len(price['attributes']) == 0:
                        if 'recurringFee' in price:
                            prices.append(price)
                            item['prices'] = price
                            break
            optionItem = item
            optionPackage = package['id']
            break
    if 'id' in optionItem:
        break

if not 'id' in optionItem:
    print("The configured option: " + option + " is not valid.")
    exit(1)

# Verifying if the configured option requires a VLan or end point IP.
requireVlan = False
requireIp = False
for category in optionItem['prices'][0]["categories"]:
    cat = category['categoryCode']
    if cat == "static_sec_ip_addresses" or cat == "static_ipv6_addresses":
        requireIp = True
    if (cat == "sov_sec_ip_addresses_pub" or
       cat == "sov_sec_ip_addresses_priv" or cat == "sov_ipv6_addresses"):
        requireVlan = True
    break

# Getting the IP address object.
ip = {}
if requireIp:
    try:
        objectMask = "mask[ipAddresses]"
        subnet = subnetService.getSubnetForIpAddress(endPointIP,
                                                     mask=objectMask)
        if not 'id' in subnet:
            print("There is no a IP address " + endPointIP +
                  " in the subnets of the account.")
            exit(1)
        else:
            for ipSubnet in subnet['ipAddresses']:
                if ipSubnet['ipAddress'] == endPointIP:
                    ip = ipSubnet
                    break
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to find the subnet. faultCode=%s, faultString=%s"
              % (e.faultCode, e.faultString))
        exit(1)

# Getting the VLan.
vlan = {}
if requireVlan:
    try:
        objectFilter = {
            "networkVlans": {
                "vlanNumber": {
                    "operation": vlanNumber
                }
            }
        }
        vlans = accountService.getNetworkVlans(filter=objectFilter)
        if len(vlans) == 0:
            print("There is no a VLan number " + str(vlanNumber) +
                  " in the account.")
            exit(1)
        else:
            vlan = vlans[0]
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to retrieve the VLans. faultCode=%s, faultString=%s" %
              (e.faultCode, e.faultString))
        exit(1)

# Creating the order template for the subnet
orderTemplate = {
    'packageId': optionPackage,
    'prices': optionItem['prices'],
    'quantity': 1,
    'complexType': 'SoftLayer_Container_Product_Order_Network_Subnet'
}

if requireVlan:
    orderTemplate['endPointVlanId'] = vlan['id']
elif requireIp:
    orderTemplate['endPointIpAddressId'] = ip['id']

try:
    # verifyOrder() will check your order for errors. Replace this with a call
    # to placeOrder() when you're ready to order. Both calls return a receipt
    # object that you can use for your records.
    result = orderService.verifyOrder(orderTemplate)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" %
          (e.faultCode, e.faultString))

```
