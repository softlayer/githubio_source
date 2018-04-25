---
title: "place_order_block_storage_endurance_with_snapshot_size.py"
description: "place_order_block_storage_endurance_with_snapshot_size.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Storage_Iscsi_"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Location"
    - "SoftLayer_Container_Product_Order_Network_Storage_Enterprise"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Location_Group_Pricing"
    - "SoftLayer_Product_Order"
tags:
    - "endurance"
---


```
"""
Order a block storage (endurance) with snapshot storage space.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing/getAllObjects
http://sldn.softlayer.com/reference/services/SoftLayer_Location
http://sldn.softlayer.com/reference/services/SoftLayer_Location/getDatacenters
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Enterprise
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/blog/cmporter/Location-based-Pricing-and-You
http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-3
http://sldn.softlayer.com/node/274081
http://sldn.softlayer.com/article/Python
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# Values "AMS01", "AMS03", "CHE01", "DAL05", "DAL06" "FRA02", "HKG02", "LON02", etc.
location = "set me"

# Values: "0.25", "2", "4"
iops = "set me"

# Values "20", "40", "80", "100", etc.
storageSize = "set me"

# Values "0", "5", "10", "20", "40", etc.
# Remember that the values must not exceed the size of the configured storage size.
snapshotSize = "set me"

# Values "Hyper-V", "Linux", "VMWare", "Windows 2008+", "Windows GPT", "Windows 2003", "Xen"
os = "set me"

PACKAGE_ID = 240

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']
packageService = client['SoftLayer_Product_Package']
locationGroupService = client['SoftLayer_Location_Group_Pricing']
locationService = client['SoftLayer_Location']
osService = client['SoftLayer_Network_Storage_Iscsi_OS_Type']

objectFilterDatacenter = {"name": {"operation": location.lower()}}
objectFilterStorageEnterprise = {"items": {"categories": {"categoryCode": {"operation": "storage_service_enterprise"}}}}
objectFilterFileStorage = {"items": {"categories": {"categoryCode": {"operation": "storage_block"}}}}
objectFilterOsType = {"name": {"operation": os}}
objectMaskLocation = "mask[locations]"
objectMaskIops = "mask[attributes]"


try:
    # Getting the datacenter.
    datacenter = locationService.getDatacenters(filter=objectFilterDatacenter)
    # Getting file storage prices.
    itemsFileStorage = packageService.getItems(id=PACKAGE_ID, filter=objectFilterFileStorage)
    # Getting the item prices whose category is storage_service_enterprise.
    itemsStorageEnterprise = packageService.getItems(id=PACKAGE_ID, filter=objectFilterStorageEnterprise)
    # Getting the SoftLayer_Location_Group_Pricing which contains the configured location.
    locations = locationGroupService.getAllObjects(mask=objectMaskLocation)
    for item in locations:
        for loc in item['locations']:
            if location.lower() == loc['name'].lower():
                location = item
                break
        if 'id' in location:
            break
    # Getting the IOPS item prices which are equals to the configured IOPS, and are valid for the configured location.
    # In case we did not get a location group for the configured location
    # we are going to search for standard prices.
    if 'id' in location:
        objectFilterLocation = {"items": {"description": {"operation": iops + " IOPS per GB"}, "categories": {"categoryCode": {"operation": "storage_tier_level"}}, "locationGroupId": {"operation": "in", "options": [{"name": "data", "value": [location['id']]}]}}}
        objectFilter = objectFilterLocation
    else:
        objectFilterNoLocation = {"items": {"description": {"operation":  iops + " IOPS per GB"}, "categories": {"categoryCode": {"operation": "storage_tier_level"}}, "locationGroupId": {"operation": "is null"}}}
        objectFilter = objectFilterNoLocation
    itemsIops = packageService.getItems(id=PACKAGE_ID, filter=objectFilter, mask=objectMaskIops)
    if len(itemsIops) == 0:
        # In case we got an empty list we try getting the standard prices
        objectFilter = {"items": {"description": {"operation": iops + " IOPS per GB"}, "categories": {"categoryCode": {"operation": "storage_tier_level"}}, "locationGroupId": {"operation": "is null"}}}
        itemsIops = packageService.getItems(id=PACKAGE_ID, filter=objectFilter, mask=objectMaskIops)
    # Getting the storage space which are equals to the configured storage space, meet the requirements for the configured IOPS, and are valid for the configured location
    # In case we did not get a location group for the configured location
    # we are going to search for standard prices.
    if 'id' in location:
        objectFilterLocation = {"items": {"capacity": {"operation":  storageSize}, "prices": {"capacityRestrictionMaximum": {"operation": itemsIops[0]['attributes'][0]['value']}, "categories": {"categoryCode": {"operation": "performance_storage_space"}}, "locationGroupId": {"operation": "in", "options": [{"name": "data", "value": [location['id']]}]}}}}
        objectFilter = objectFilterLocation
    else:
        objectFilterNoLocation = {"items": {"capacity": {"operation":  storageSize}, "prices": {"capacityRestrictionMaximum": {"operation": itemsIops[0]['attributes'][0]['value']}, "categories": {"categoryCode": {"operation": "performance_storage_space"}}, "locationGroupId": {"operation": "is null"}}}}
        objectFilter = objectFilterNoLocation
    itemsStorage = packageService.getItems(id=PACKAGE_ID, filter=objectFilter)
    if len(itemsStorage) == 0:
        # In case we got an empty list we try getting the standard prices
        objectFilter = {"items": {"capacity": {"operation": storageSize}, "prices": {"capacityRestrictionMaximum": {"operation": itemsIops[0]['attributes'][0]['value']}, "categories": {"categoryCode": {"operation": "performance_storage_space"}}, "locationGroupId": {"operation": "is null"}}}}
        itemsStorage = packageService.getItems(id=PACKAGE_ID, filter=objectFilter)
    # Getting the snapshot storage space which are equals to the configured snapshot storage space, meet the requirements for the configured IOPS, and are valid for the configured location
    # In case we did not get a location group for the configured location
    # we are going to search for standard prices.
    if 'id' in location:
        objectFilterLocation = {"items": {"capacity": {"operation":  snapshotSize}, "prices": {"capacityRestrictionMaximum": {"operation": itemsIops[0]['attributes'][0]['value']}, "categories": {"categoryCode": {"operation": "storage_snapshot_space"}}, "locationGroupId": {"operation": "in", "options": [{"name": "data", "value": [location['id']]}]}}}}
        objectFilter = objectFilterLocation
    else:
        objectFilterNoLocation = {"items": {"capacity": {"operation":  snapshotSize}, "prices": {"capacityRestrictionMaximum": {"operation": itemsIops[0]['attributes'][0]['value']}, "categories": {"categoryCode": {"operation": "storage_snapshot_space"}}, "locationGroupId": {"operation": "is null"}}}}
        objectFilter = objectFilterNoLocation
    itemsSnapshot = packageService.getItems(id=PACKAGE_ID, filter=objectFilter)
    if len(itemsStorage) == 0:
        # In case we got an empty list we try getting the standard prices
        objectFilter = {"items": {"capacity": {"operation": snapshotSize}, "prices": {"capacityRestrictionMaximum": {"operation": itemsIops[0]['attributes'][0]['value']}, "categories": {"categoryCode": {"operation": "storage_snapshot_space"}}, "locationGroupId": {"operation": "is null"}}}}
        itemsSnapshot = packageService.getItems(id=PACKAGE_ID, filter=objectFilter)
    # Getting the OS
    os = osService.getAllObjects(filter=objectFilterOsType)
    # Building the order template
    orderData = {
        "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise",
        "packageId": PACKAGE_ID,
        "location": datacenter[0]['id'],
        "quantity": 1,
        "prices": [
            {
                "id": itemsFileStorage[0]['prices'][0]['id']
            },
            {
                "id": itemsStorageEnterprise[0]['prices'][0]['id']
            },
            {
                "id": itemsIops[0]['prices'][0]['id']
            },
            {
                "id": itemsStorage[0]['prices'][0]['id']
            },
            {
                "id": itemsSnapshot[0]['prices'][0]['id']
            }
        ],
        "osFormatType": os[0]
    }
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderData)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
