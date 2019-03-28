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

Upgrade CPU, RAM.
To get the items KeyNames available to upgrade your VSI, you can use the service
SoftLayer_Virtual_Guest::getUpgradeItemPrices. Add to your request a mask as the below to retrieve the items KeyNames.
mask[id,item[id,keyName,description]

I suggest you to search the items comparing with the control portal, use the description and search in the response,
then use the keyName of that item.

Change the "items" variable with the cpu and ram keyNames you want to upgrade your vs.
e.g. I am upgrading the cpu from 2 x 2.0 GHz to 8 x 2.0 GHz and the ram from 4 GB to 12 GB.
```
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111

# Package keyName.
package_keyName = 'CLOUD_SERVER'

# items KeyNames to be upgraded.
items = ['GUEST_PRIVATE_CORES_8', 'RAM_12_GB']

object_filter = {'keyName': {'operation': package_keyName}}

response_package = client["SoftLayer_Product_Package"].getAllObjects(filter=object_filter)
package_id = response_package[0]['id']

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
    'packageId': package_id,
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

Upgrade a VSI adding two new disks.

Replace the "virtualGuestId" variable with your vsId and set the disks variables with the keyName of the disk you want,
that's in the bottom of the script.
You can add the disks you want to your vs e.g. disk1, disk2, disk3, disk4.
The disk0 is added when you create your vs and you can only change this disk from SAN to LOCAL.

```
import json

import SoftLayer


class example():
    def __init__(self):
        # Declare the API client
        self.client = SoftLayer.create_client_from_env()

    def get_item_price_id(self, virtualGuestId, disk_keyName):
        item_prices = self.client["SoftLayer_Virtual_Guest"].getUpgradeItemPrices(mask='mask[id,item[id,keyName]]',
                                                                                  id=virtualGuestId)
        item_priceId = None
        for get_item in item_prices:
            if disk_keyName == get_item['item']['keyName']:
                item_priceId = get_item['id']

        return item_priceId

    def build_item_price(self, item_price_id, categoryCode):

        item_object = {'id': item_price_id,
                       'categories': [
                           {
                               'categoryCode': categoryCode,
                               'complexType': 'SoftLayer_Product_Item_Category'
                           }
                       ],
                       }
        return item_object

    def get_packageId(self):
        # Package keyName
        package_keyName = 'CLOUD_SERVER'

        object_filter = {'keyName': {'operation': package_keyName}}

        response_package = self.client["SoftLayer_Product_Package"].getAllObjects(filter=object_filter)
        package_id = response_package[0]['id']

        return package_id

    def add_disks(self, virtualGuestId, disk1=None, disk2=None, disk3=None, disk4=None):

        prices = []
        if disk1 is not None:
            item_priceId = self.get_item_price_id(virtualGuestId, disk1)
            item_price_object = self.build_item_price(item_priceId, 'guest_disk1')
            prices.append(item_price_object)

        if disk2 is not None:
            item_priceId = self.get_item_price_id(virtualGuestId, disk2)
            item_price_object = self.build_item_price(item_priceId, 'guest_disk2')
            prices.append(item_price_object)

        if disk3 is not None:
            item_priceId = self.get_item_price_id(virtualGuestId, disk3)
            item_price_object = self.build_item_price(item_priceId, 'guest_disk3')
            prices.append(item_price_object)

        if disk4 is not None:
            item_priceId = self.get_item_price_id(virtualGuestId, disk4)
            item_price_object = self.build_item_price(item_priceId, 'guest_disk4')
            prices.append(item_price_object)

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
            'packageId': self.get_packageId(),
            'prices': prices,
            'properties': properties,
            'virtualGuests': virtualGuests
        }

        try:
            # Upgrading the virtual guest
            response = self.client['SoftLayer_Product_Order'].verifyOrder(orderData)
            print(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))
        except SoftLayer.SoftLayerAPIError as e:
            """
            If there was an error returned from the SoftLayer API then bomb out with the
            error message.
            """
            print("Unable to upgrade VSI faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))


if __name__ == "__main__":
    # The id of the virtual guest you wish upgrade
    virtualGuestId = 11111

    # Disk keyName.
    disk1 = 'GUEST_DISK_10_GB_SAN'

    disk4 = 'GUEST_DISK_20_GB_SAN'

    # Start the script
    main = example()

    main.add_disks(virtualGuestId, disk1=disk1, disk4=disk4)

```

Upgrade the size of a specific disk.
Change the "item_keyName" variable with the disk keyName you want to upgrade the specific disk on your vs.
e.g. I am upgrading the first disk from 10 GB to 20 GB.
```
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 11111

# Package keyName.
package_keyname = 'CLOUD_SERVER'

# item KeyName to be upgraded.
item_keyName = 'GUEST_DISK_20_GB_SAN'  # "description": "20 GB (SAN)"

object_filter = {'keyName': {'operation': package_keyname}}

response_package = client["SoftLayer_Product_Package"].getAllObjects(filter=object_filter)
package_id = response_package[0]['id']

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
    'packageId': package_id,
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

Upgrade the BANDWIDTH (Monthly).
This option is only available for a vs monthly.

Change the "items" variable with the item keyName you want to upgrade your vs.
e.g. I am upgrading the Bandwidth from 250 GB to 1000 GB.
```
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 12345

# Package keyName.
package_keyName = 'CLOUD_SERVER'

# Item KeyName to be upgraded.
items = ['BANDWIDTH_1000_GB'] # "description": "1000 GB Bandwidth Allotment"

object_filter = {'keyName': {'operation': package_keyName}}

response_package = client["SoftLayer_Product_Package"].getAllObjects(filter=object_filter)
package_id = response_package[0]['id']

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
    'packageId': package_id,
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

Upgrade the  Uplink Port Speeds.
Change the "items" variable with the item keyName you want to upgrade your vs.
e.g. I am upgrading the Uplink Port Speeds from 1 Gbps to 100 Mbps.
```
import json

import SoftLayer

# Declare the API client
client = SoftLayer.create_client_from_env()

# The id of the virtual guest you wish upgrade
virtualGuestId = 12345

# Package keyName.
package_keyName = 'CLOUD_SERVER'

# items KeyNames to be upgraded.
items = ['100_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS']  # "description": "100 Mbps Public & Private Network Uplinks"

object_filter = {'keyName': {'operation': package_keyName}}

response_package = client["SoftLayer_Product_Package"].getAllObjects(filter=object_filter)
package_id = response_package[0]['id']

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
    'packageId': package_id,
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
