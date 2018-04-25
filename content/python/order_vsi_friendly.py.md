---
title: "order_vsi_friendly.py"
description: "order_vsi_friendly.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Location"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "virtualserver"
---


```
"""
Order a new VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSshKeys
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/services/SoftLayer_Location/getDatacenters
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Declare variables
location = "AMS01"
quantity = 1
# If you want the VSI hourly pricing
# set the value as True
useHourlyPricing = False

# The configuration of the VSI
# The values and names are the same like
# the ones displayed in the portal.
configuration = {
    "COMPUTING INSTANCE": "2 x 2.0 GHz Cores",
    "RAM": "4 GB",
    "OPERATING SYSTEM": "CentOS 7.x - Minimal Install (64 bit)",
    "FIRST DISK": "25 GB (SAN)",
    "PUBLIC BANDWIDTH": "250 GB Bandwidth",
    "UPLINK PORT SPEEDS": "100 Mbps Public & Private Network Uplinks",
    "MONITORING": "Host Ping",
    "RESPONSE": "Automated Notification",
    "Primary IP Addresses": "1 IP Address",
    "Remote Management": "Reboot / Remote Console",
    "Notification": "Email and Ticket",
    "VPN Management - Private Network": "Unlimited SSL VPN Users & 1 PPTP VPN User per account",
    "Vulnerability Assessments & Management": "Nessus Vulnerability Assessment & Reporting"
}

# Specifies the hostname and domain we want for our VSI.
# If you set quantity greater than 1 then you
# need to define one hostname/domain pair per VSI you wish to order.
virtualGuest = [
    {
        "domain": "softlayer.ibm.com",
        "hostname": "VM1",
        # The vlan configuration for the VSI if you do not wish to configure
        # the vlans just comment the lines.
        # set the any IP address which belongs to the VLAN you wish to configure in the VSI
        "backendVlanIp": "10.68.117.193",
        "frontedVLAN": "159.122.23.225"
    }
]

# The post install script to apply.
# Leave in empty if you do not wish to apply an script in the provisioning.
postInstallScript = ""

# The list of ssh keys to apply to the VSI.
# Set the label names of the ssh keys like in the portal
# Leave in empty if you do not wish to apply any ssh key.
sshKeys = ["labkey", "matt-sl-test"]


PACKAGE = 46
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
orderService = client['SoftLayer_Product_Order']
accountService = client['SoftLayer_Account']
packageService = client['SoftLayer_Product_Package']
locationService = client['SoftLayer_Location']
valnService = client['SoftLayer_Network_Vlan']

try:
    location = locationService.getDatacenters(filter={"name": {"operation": location.lower()}})
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the datacenter. " % (e.faultCode, e.faultString))
    exit(0)

try:
    pricesPackage = packageService.getItemPrices(id=PACKAGE, mask="mask[categories, item]")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the item prices. " % (e.faultCode, e.faultString))
    exit(0)

# Getting the item prices for the order.
prices = []
for item in configuration.keys():
    for price in pricesPackage:
        added = False
        if 'categories' in price:
            for category in price['categories']:
                if category['name'].strip().upper() == item.strip().upper() and \
                   price['item']['description'].strip().upper() == configuration[item].strip().upper() and \
                   price['locationGroupId'] == "":
                    prices.append(price)
                    added = True
                    break
            if added:
                break
    if not added:
        print("There is no price for the item: " + item + "- " + configuration[item])
        exit(0)

vsis = []
for vsi in virtualGuest:
    guest = {}
    if 'domain' in vsi:
        guest['domain'] = vsi['domain']
    if 'hostname' in vsi:
        guest['hostname'] = vsi['hostname']
    if 'backendVlanIp' in vsi:
        try:
            backend = valnService.getVlanForIpAddress(vsi['backendVlanIp'])
            guest['primaryBackendNetworkComponent'] = {}
            guest['primaryBackendNetworkComponent']['networkVlan'] = backend
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the backend Vlan. " % (e.faultCode, e.faultString))
    if 'frontedVLAN' in vsi:
        try:
            fronted = valnService.getVlanForIpAddress(vsi['frontedVLAN'])
            guest['primaryNetworkComponent'] = {}
            guest['primaryNetworkComponent']['networkVlan'] = fronted
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the fronted Vlan. " % (e.faultCode, e.faultString))
    vsis.append(guest)


orderData = {
    "prices": prices,
    "packageId": PACKAGE,
    "location": location[0]['id'],
    'hardware': vsis,
    'useHourlyPricing': useHourlyPricing
}

if postInstallScript:
    orderData['provisionScripts'] = [postInstallScript]

if len(sshKeys) > 0:
    objectfilter = {"sshKeys": {"label": {"operation": "in", "options": [{"name": "data", "value": sshKeys}]}}}
    try:
        sshs = accountService.getSshKeys(filter=objectfilter, mask="mask[id]")
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the ssh keys. " % (e.faultCode, e.faultString))
    if len(sshs) > 0:
        orderData['sshKeys'] = []
        sshKeyIds = {}
        sshKeyIds['sshKeyIds'] = []
        for ssh in sshs:
            sshKeyIds['sshKeyIds'].append(ssh['id'])
        orderData['sshKeys'].append(sshKeyIds)
    else:
        print("None ssh key was found")

try:
    # When you are ready to order the VSI
    # change verifyOrder() method by placeOrder() method.
    result = orderService.verifyOrder(orderData)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the order. "
          % (e.faultCode, e.faultString))

```
