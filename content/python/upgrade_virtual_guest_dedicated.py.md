---
title: "Working with upgrade virtual guest dedicated and families"
description: "A few examples on interacting with upgrade virtual guest dedicated and families."
date: "2019-03-29"
classes:
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
tags:
    - "virtualserver"
    - "upgrade"
    - "upgradevirtualguest"
---

### Upgrade CPU, RAM for VSI dedicated.

To get the items KeyNames available to upgrade your VSI, you can use the service
SoftLayer_Virtual_Guest::getUpgradeItemPrices. Add to your request a mask as the below to retrieve the items KeyNames.

```mask[id,item[id,keyName,description]```

I suggest you to search the items comparing with the control portal, use the description and search in the response,
then use the keyName of that item.

Change the "items" variable with the cpu and ram keyNames you want to upgrade your vs.
e.g. I am upgrading the cpu from 2 x 2.0 GHz to 8 x 2.0 GHz and the ram from 4 GB to 12 GB.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111

# items KeyNames to be upgraded.
items = ['GUEST_PRIVATE_CORES_8', 'RAM_12_GB']

item_prices = client["SoftLayer_Virtual_Guest"].getUpgradeItemPrices(mask='mask[id,item[id,keyName]]',
                                                                     id=virtualGuestId)

prices = []
for item in items:
    for get_item in item_prices:
        if item == get_item['item']['keyName']:
            prices.append(get_item['id'])

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        "name": "MAINTENANCE_WINDOW",
        "value": "2018-08-20T06:04:10Z"},
    {
        "name": "NOTE_GENERAL",
        "value": "Upgrade instance configuration."
    }
]

# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuests = [
    {
        "id": virtualGuestId
    }
]

"""
Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade object
containing the upgrade you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
    'prices': [{'id': price_id} for price_id in prices],
    'properties': properties,
    'virtualGuests': virtualGuests
}

try:
    # Upgrading the virtual guest
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade the VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Upgrade a flavor(cpu, ram) for VSI families.

Change the "preset_keyName" variable with the flavor keyNames you want to upgrade your vs.

e.g. I am upgrading the flavor BL2_4X8X100(cpu 4, ram 8 GB, first disk 100 GB) to
BL2_4X16X100(cpu 4, ram 16 GB, first disk 100 GB).

The flavor keyName you can get through SoftLayer_Product_Package::getActivePresets.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 12345

# Package keyName.
package_keyName = 'PUBLIC_CLOUD_SERVER'

# Preset keyName cpu 4, ram 16 GB, first disk 100 GB.
preset_keyName = 'BL2_4X16X100'

object_filter = {'keyName': {'operation': package_keyName}}

filter_preset = {'activePresets': {'keyName': {'operation': preset_keyName}}}

response_package = client["SoftLayer_Product_Package"].getAllObjects(filter=object_filter)
package_id = response_package[0]['id']

response_preset = client["SoftLayer_Product_Package"].getActivePresets(filter=filter_preset, id=package_id)
presetId = response_preset[0]['id']

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        "name": "orderOrigin",
        "value": "control"
    },

    {
        "name": "MAINTENANCE_WINDOW",
        "value": "2018-08-31T16:42:52.370Z"
    }
]

# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuests = [
    {
        "id": virtualGuestId
    }
]

"""
Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade object
containing the upgrade you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
    'presetId': presetId,
    'properties': properties,
    'virtualGuests': virtualGuests
}

try:
    # Upgrading the virtual guest
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade the VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Adding two new disks (This script works for both options, VSI dedicated and families).

Replace the "virtualGuestId" variable with your vsId and set the "items" data with the keyName of the disk size you
choose.

You can set the "guest_disk" depend of the position of the disk you want e.g. guest_disk1, guest_disk2, guest_disk3,
guest_disk4.

The disk0 is added when you create your vs and you can only change this disk from SAN to LOCAL.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 12345

# Items keyName. Change the "guest_disk" position as you want, to add to the vs, e.g. for guest_disk3, guest_disk4 too.
items = {'GUEST_DISK_10_GB_SAN': 'guest_disk1', 'GUEST_DISK_20_GB_SAN': 'guest_disk2'}

item_prices = client["SoftLayer_Virtual_Guest"].getUpgradeItemPrices(mask='mask[id,item[id,keyName]]',
                                                                     id=virtualGuestId)

prices = []
for item in items.keys():
    for get_item in item_prices:
        if item == get_item['item']['keyName']:
            itemId = get_item['id']
            itemObject = {'id': itemId,
                          'categories': [
                              {
                                  'categoryCode': items.get(item),
                                  'complexType': 'SoftLayer_Product_Item_Category'
                              }
                          ],
                          }
            prices.append(itemObject)
            break

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        "name": "MAINTENANCE_WINDOW",
        "value": "2018-08-20T06:04:10Z"},
    {
        "name": "NOTE_GENERAL",
        "value": "Upgrade instance configuration."
    }
]

# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuests = [
    {
        "id": virtualGuestId
    }
]

orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
    'prices': prices,
    'properties': properties,
    'virtualGuests': virtualGuests
}

orderService = client['SoftLayer_Product_Order']

try:
    # Upgrading the virtual guest
    response = orderService.verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade the VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Upgrade the size of a specific disk (This script works for both options, VSI dedicated and families).

Change the "item_keyName" variable with the disk keyName you want to upgrade the specific disk on your vs.

e.g. I am upgrading the first disk from 10 GB to 20 GB.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111

# item KeyName to be upgraded.
item_keyName = 'GUEST_DISK_20_GB_SAN'  # "description": "20 GB (SAN)"

item_prices = client["SoftLayer_Virtual_Guest"].getUpgradeItemPrices(mask='mask[id,item[id,keyName]]',
                                                                     id=virtualGuestId)

prices = []
item_price_id = None
for item in item_prices:
    if item_keyName == item['item']['keyName']:
        item_price_id = item['id']

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        "name": "MAINTENANCE_WINDOW",
        "value": "2018-08-20T06:04:10Z"},
    {
        "name": "NOTE_GENERAL",
        "value": "Upgrade instance configuration."
    }
]

# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuests = [
    {
        "id": virtualGuestId
    }
]

orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
    'prices': [{'id': item_price_id,
                'categories': [
                    {
                        'categoryCode': 'guest_disk1', # Change the "categoryCode" data for the categoryCode you want.
                        'complexType': 'SoftLayer_Product_Item_Category'
                    }
                ]
                }
               ],
    'properties': properties,
    'virtualGuests': virtualGuests
}

try:
    # Upgrading the virtual guest
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade the VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Upgrade the BANDWIDTH (This script works for both options, VSI dedicated and families Monthly).

This option is only available for a vs monthly.

Change the "items" variable with the item keyName you want to upgrade your vs.

e.g. I am upgrading the Bandwidth from 250 GB to 1000 GB.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 12345

# Item KeyName to be upgraded.
items = ['BANDWIDTH_1000_GB'] # "description": "1000 GB Bandwidth Allotment"

item_prices = client["SoftLayer_Virtual_Guest"].getUpgradeItemPrices(mask='mask[id,item[id,keyName]]',
                                                                     id=virtualGuestId)

prices = []
for item in items:
    for item_price in item_prices:
        if item == item_price['item']['keyName']:
            prices.append(item_price['id'])

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        "name": "MAINTENANCE_WINDOW",
        "value": "2018-08-20T06:04:10Z"},
    {
        "name": "NOTE_GENERAL",
        "value": "Upgrade instance configuration."
    }
]

# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuests = [
    {
        "id": virtualGuestId
    }
]

orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
    'prices': [{'id': price_id} for price_id in prices],
    'properties': properties,
    'virtualGuests': virtualGuests
}

try:
    # Upgrading the virtual guest
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade the VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))


```

### Upgrade the  Uplink Port Speeds (This script works for both options VSI dedicated and families).

Change the "items" variable with the item keyName you want to upgrade your vs.

e.g. I am upgrading the Uplink Port Speeds from 1 Gbps to 100 Mbps.
```python
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 12345

# items KeyNames to be upgraded.
items = ['100_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS']  # "description": "100 Mbps Public & Private Network Uplinks"

item_prices = client["SoftLayer_Virtual_Guest"].getUpgradeItemPrices(mask='mask[id,item[id,keyName]]',
                                                                     id=virtualGuestId)

prices = []
for item in items:
    for get_item in item_prices:
        if item == get_item['item']['keyName']:
            prices.append(get_item['id'])

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        "name": "MAINTENANCE_WINDOW",
        "value": "2018-08-20T06:04:10Z"},
    {
        "name": "NOTE_GENERAL",
        "value": "Upgrade instance configuration."
    }
]

# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuests = [
    {
        "id": virtualGuestId
    }
]

orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
    'prices': [{'id': price_id} for price_id in prices],
    'properties': properties,
    'virtualGuests': virtualGuests
}

try:
    # Upgrading the virtual guest
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade the VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))


```
