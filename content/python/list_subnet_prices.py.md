---
title: "list_subnet_prices.py"
description: "list_subnet_prices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "subnets"
---


```
"""
List the options and the prices to order a subnet like the portal.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getAllObjects
http://sldn.softlayer.com/article/Object-Masks
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

client = SoftLayer.Client()
packageService = client['SoftLayer_Product_Package']

# The groups listed in the portal and its category code.
groups = {
    "Static Public": "static_sec_ip_addresses",
    "Portable Public": "sov_sec_ip_addresses_pub",
    "Portable Private": "sov_sec_ip_addresses_priv",
    "Global IPv4": "global_ipv4",
    "Static Public IPv6": "static_ipv6_addresses",
    "Portable Public IPv6": "sov_ipv6_addresses",
    "Global IPv6": "global_ipv6"
}

# Declaring a filter to get the packages related to subnets
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
objectMask = "mask[items[id, description, prices[id, recurringFee, attributes], categories[categoryCode]]]"

try:
    packages = packageService.getAllObjects(filter=objectFilter, mask=objectMask)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the packages. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

options = []
for group in groups.keys():
    option = {}
    option['category'] = group
    option['items'] = []
    for package in packages:
        for item in package['items']:
            newOpItem = True
            for opItem in option['items']:
                if opItem['id'] == item['id']:
                    newOpItem = False
                    break
            if newOpItem:
                for category in item['categories']:
                    if category['categoryCode'] == groups[group]:
                        prices = []
                        if len(item['prices']) > 1:
                            for price in item['prices']:
                                if len(price['attributes']) == 0:
                                    if 'recurringFee' in price:
                                        prices.append(price)
                                        item['prices'] = price
                                        break
                        option['items'].append(item)
                        break
    options.append(option)

print(json.dumps(options, sort_keys=True, indent=2, separators=(',', ': ')))

```
