---
title: "list_iscsi_storage.py"
description: "list_iscsi_storage.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Storage"
tags:
    - "iscsi"
---


```
"""
List Storage iSCSI.
This script will list the Storage iSCSI available in the account

See below references for more details.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getIscsiNetworkStorage
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

from prettytable import PrettyTable

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'

# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

# Mask to get the location of Network Storage
objectMask = 'mask[billingItem[location]]'
# Get the list of iSCSI storage
storages = client['Account'].getIscsiNetworkStorage(mask=objectMask)

table = []

# Let's to iterate through the list storage to get the details of each storage.
for storage in storages:
    table.append(
        [storage['username'], storage['nasType'], storage['serviceResourceBackendIpAddress'], storage['capacityGb'],
         storage['billingItem']['location']['longName']])

storageDetails = PrettyTable(['Name', 'Type', 'Target IP address', 'Capacity GB', 'Location'])
storageDetails.align['ID'] = 'l'
storageDetails.padding_width = 1
for row in table:
    storageDetails.add_row([row[0], row[1], row[2], row[3], row[4]])
print(storageDetails)

```
