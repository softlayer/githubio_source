---
title: "get_locations.py"
description: "get_locations.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Get package location.

This script will retrieve a collection of valid locations for a given package
by calling to SoftLayer_Product_Package::getLocations method.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getLocations
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# So we can talk to the SoftLayer API:
import SoftLayer

# For nice output:
from prettytable import PrettyTable

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'
API_KEY = 'set-me'
package = 46

# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Get the location for the given package
locations = client['SoftLayer_Product_Package'].getLocations(id=package)

table = []
for location in locations:
    table.append([location['id'], location['longName'], location['statusId']])
locationDetail = PrettyTable(["ID", "Location description", "Status ID"])
locationDetail.align["ID"] = "l"
locationDetail.padding_width = 1
for row in table:
    locationDetail.add_row([row[0], row[1], row[2]])
print(locationDetail)

```
