---
title: "Working with upgrade virtual guest dedicated"
description: "A few examples on interacting with upgrade virtual guest."
date: "2019-03-27"
classes:
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
tags:
    - "virtualserver"
---

Upgrade a VSI(cpu, ram)
```
import json

import SoftLayer

client = SoftLayer.create_client_from_env()
orderService = client['SoftLayer_Product_Order']

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111

# Package keyName.
package_keyname = 'CLOUD_SERVER'

object_mask = 'mask[prices]'

# items KeyNames to be upgrade
items = ['GUEST_PRIVATE_CORES_8', 'RAM_12_GB']

response_package = client["SoftLayer_Product_Package"].getAllObjects()

package_id = None
for val in response_package:
    if val.get('keyName') == package_keyname:
        package_id = val.get('id')

get_item_id_price = client["SoftLayer_Product_Package"].getItems(mask=object_mask, id=package_id)

prices = []
for keyname_item in items:
    for get_item in get_item_id_price:
        if keyname_item == get_item.get('keyName'):
            prices.append(get_item['prices'][0]['id'])

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
    'packageId': package_id,
    'prices': [{'id': price_id} for price_id in prices],
    'properties': properties,
    'virtualGuests': virtualGuests
}

try:
    # Upgrading the virtual guest
    response = orderService.verifyOrder(orderData)
    print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    """
        If there was an error returned from the SoftLayer API then bomb out with the
        error message.
        """
    print("Unable to upgrade VSI \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))


```

Upgrade a VSI adding two new disks.
```
import json

import SoftLayer

client = SoftLayer.create_client_from_env()

mask_prices = 'mask[prices[categories]]'

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111

# Package keyName.
package_keyname = 'CLOUD_SERVER'

# items KeyNames to be upgrade
items_list = ['GUEST_DISK_10_GB_SAN',  # "description": "10 GB (SAN)", "categoryCode": "guest_disk1"
                  'GUEST_DISK_20_GB_SAN'  # "description": "20 GB (SAN)", "categoryCode": "guest_disk2"
              ]

response_package = client["SoftLayer_Product_Package"].getAllObjects()
package_id = 0
for val in response_package:
    if val.get('keyName') == package_keyname:
        package_id = val.get('id')

item_prices = client["SoftLayer_Product_Package"].getItems(mask=mask_prices, id=package_id)

prices = []
for keyname_item in items_list:
    for item in item_prices:
        if keyname_item == item.get('keyName'):
            prices.append(item['prices'][0]['id'])

print(' '.join(map(str, prices)))

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
    'packageId': package_id,
    'prices': [{'id': prices[0],
                'categories': [
                    {
                        'categoryCode': 'guest_disk1',
                        'complexType': 'SoftLayer_Product_Item_Category'
                    }
                ],
                },
               {
                   'id': prices[1],
                   'categories': [
                       {
                           'categoryCode': 'guest_disk2',
                           'complexType': 'SoftLayer_Product_Item_Category'
                       }
                   ],
               }

               ],
    'properties': properties,
    'virtualGuests': virtualGuests
}

orderService = client['SoftLayer_Product_Order']

try:
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

Upgrade a VSI changing the size of a specific disk.
```
import json

import SoftLayer

client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111
mask_prices = 'mask[prices]'
package_keyname = 'CLOUD_SERVER'

# items KeyNames to be upgrade
item_keyName_list = ['GUEST_DISK_20_GB_SAN'] # "description": "20 GB (SAN)", "categoryCode": "guest_disk2"

response_package = client["SoftLayer_Product_Package"].getAllObjects()
package_id = 0
for package in response_package:
    if package.get('keyName') == package_keyname:
        package_id = package.get('id')

item_list = client["SoftLayer_Product_Package"].getItems(mask=mask_prices, id=package_id)

prices = []
for keyname_item in item_keyName_list:
    for item in item_list:
        if keyname_item == item.get('keyName'):
            prices.append(item['prices'][0]['id'])

print(' '.join(map(str, prices)))

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
    'packageId': package_id,
    'prices': [{'id': prices[0],
                'categories': [
                    {
                        'categoryCode': 'guest_disk1',
                        'complexType': 'SoftLayer_Product_Item_Category'
                    }
                ]
                }
               ],
    'properties': properties,
    'virtualGuests': virtualGuests
}

orderService = client['SoftLayer_Product_Order']

try:
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

Upgrade the BANDWIDTH of a VSI.
```
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env(USERNAME, API_KEY)

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111
object_mask = 'mask[prices]'
package_keyname = 'CLOUD_SERVER'

# items KeyNames to be upgrade
item_keyName_list = ['BANDWIDTH_1000_GB'] # "keyName": "BANDWIDTH_1000_GB", "description": "1000 GB Bandwidth Allotment"

response_package = client["SoftLayer_Product_Package"].getAllObjects()
package_id = 0
for val in response_package:
    if val.get('keyName') == package_keyname:
        package_id = val.get('id')

get_item_id_price = client["SoftLayer_Product_Package"].getItems(mask=object_mask, id=package_id)

prices = []
for keyname_item in item_keyName_list:
    for get_item in get_item_id_price:
        if keyname_item == get_item.get('keyName'):
            prices.append(get_item['prices'][0]['id'])

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
    'packageId': package_id,
    'prices': [{'id': price_id} for price_id in prices],
    'properties': properties,
    'virtualGuests': virtualGuests
}

orderService = client['SoftLayer_Product_Order']

try:
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

Upgrade the  Port Speed of a VSI.
```
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111
package_keyname = 'CLOUD_SERVER'
object_mask = 'mask[prices]'

# items KeyNames to be upgrade
item_keyName_list = [
    '100_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS']  # "description": "100 Mbps Public & Private Network Uplinks"

response_package = client["SoftLayer_Product_Package"].getAllObjects()
package_id = 0
for package in response_package:
    if package.get('keyName') == package_keyname:
        package_id = package.get('id')

item_list = client["SoftLayer_Product_Package"].getItems(mask=object_mask, id=package_id)

prices = []
for keyname_item in item_keyName_list:
    for get_item in item_list:
        if keyname_item == get_item.get('keyName'):
            prices.append(get_item['prices'][0]['id'])

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
    'packageId': package_id,
    'prices': [{'id': price_id} for price_id in prices],
    'properties': properties,
    'virtualGuests': virtualGuests
}

orderService = client['SoftLayer_Product_Order']

try:
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
