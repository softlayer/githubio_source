---
title: "list_prices_packages_and_datacenters.py"
description: "list_prices_packages_and_datacenters.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "package"
---


```
"""
List Prices for Packages and Data centers

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getActivePackages
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getAllObjects
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getAvailableLocations

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
username = 'set me'
key = 'set me'

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client(username=username, api_key=key)
accountService = client['SoftLayer_Account']
productPackageService = client['SoftLayer_Product_Package']

try:
    # Get all active packages for your account, but this method is slow
    result = accountService.getActivePackages()
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the packages faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    # Get all packages
    result = productPackageService.getAllObjects()
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the packages faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    # Get the VSIs available to order
    packageID = 46
    result = productPackageService.getItems(id=packageID)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the items faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    # Getting the valid locations or data center for a package
    # Object mask to get the name of the data centers
    objectMask = "mask[location]"
    result = productPackageService.getAvailableLocations(mask=objectMask, id=packageID)
    print(result);
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the data centers faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
