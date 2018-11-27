---
title: "Order an endurance storage (block/file)"
description: "Shows how to order endurance storage devices"
date: "2018-11-23"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Storage_Iscsi"
    - "SoftLayer_Container_Product_Order_Network_Storage_Enterprise"   
tags:
    - "order"
    - "storage"
    - "endurance"    
---

### **Important Note:** There is a new version of storage devices (STaaS v2) so it is recomended to review [Order Block/File storages with Managers](../order_block_file_storage_with_managers)

Endurance Block/File storage devices are under package 240, the complexType is `SoftLayer_Container_Product_Order_Network_Storage_Enterprise` for both of them have in the order template.

<br />
**Tips before ordering**

In most of the cases the order verification fails whether the selected price cannot be ordered in the selected location or it does not meet the capacity restriction of the tier level.

Following REST call retrieves all prices under package 240 and shows on which locations are available, if `locationGroupId` is null means the price is standard and can be used on any location.

```html
https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/240/getItemPrices?objectMask=mask[id,capacityRestrictionMaximum,capacityRestrictionMinimum,capacityRestrictionType,locationGroupId,item[capacity,description],categories,pricingLocationGroup[locations]]
```

About capacity restrictions, the `performance_storage_space` and `storage_snapshot_space` prices have capacity restrictions (min/max) which should match with the `capacity` value of the selected `storage_tier_level` item, it means if the the item price "4 IOPS per GB" was selected and it has capacity of 300:

```json
    {
        "id": 45088,
        "locationGroupId": null,
        "categories": [
            {
                "categoryCode": "storage_tier_level",
                "id": 396,
                "name": "Storage Tier Level",
                "quantityLimit": 0,
                "sortOrder": null
            }
        ],
        "item": {
            "capacity": "300",
            "description": "4 IOPS per GB"
        }
    },
```

Then price of `performance_storage_space` should be:

```json
    {
        "id": 45138,
        "locationGroupId": null,
        "capacityRestrictionMaximum": "300",
        "capacityRestrictionMinimum": "300",
        "capacityRestrictionType": "STORAGE_TIER_LEVEL",
        "categories": [
            {
                "categoryCode": "performance_storage_space",
                "id": 382,
                "name": "Storage Space",
                "quantityLimit": 0,
                "sortOrder": null
            }
        ],
        "item": {
            "capacity": "20",
            "description": "20 GB Storage Space"
        }
    },
```

## **Block Endurance Storage**

```python
import SoftLayer
from pprint import pprint

# Building an skeleton SoftLayer_Container_Product_Order_Network_Storage_Enterprise to the order
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise",
    "location": "DALLAS05",
    "quantity": 1,
    "packageId": 240,
    # To see the list of prices available for the package
    # use the SoftLayer_Product_Package::getItems method with masks
    # or SoftLayer_Product_Package::getItemPrices
    "prices": [
        {"id": 45098},      # Block Storage         keyName: storage_block
        {"id": 45058},      # Endurance Storage     keyName: storage_service_enterprise
        {"id": 45138},      # 20 GB Storage Space   keyName: performance_storage_space
        {"id": 45088},      # 4 IOPS per GB         keyName: storage_tier_level
        {"id": 46140}       # 5 GB Storage Space    keyName: storage_snapshot_space
    ],
    "osFormatType": {"keyName": "LINUX"}
}

# Declares the API client
client = SoftLayer.Client()

try:
    # Use placeOrder method when you ready to order
    result = client['SoftLayer_Product_Order'].verifyOrder(orderTemplate)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. %s, %s" % (e.faultCode, e.faultString))

```

## **File Endurance Storage**

Since the prices are the same, basically it is only to required change the price of `storage_block` by `storage_file`, and remove the property `osFormatType`

```python
import SoftLayer
from pprint import pprint

# Building an skeleton SoftLayer_Container_Product_Order_Network_Storage_Enterprise to the order
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise",
    "location": "DALLAS05",
    "quantity": 1,
    "packageId": 240,
    # To see the list of prices available for the package
    # use the SoftLayer_Product_Package::getItems method with masks
    # or SoftLayer_Product_Package::getItemPrices
    "prices": [
        {"id": 45108},      # File Storage          keyName: storage_file
        {"id": 45058},      # Endurance Storage     keyName: storage_service_enterprise
        {"id": 45138},      # 20 GB Storage Space   keyName: performance_storage_space
        {"id": 45088},      # 4 IOPS per GB         keyName: storage_tier_level
        {"id": 46140}       # 5 GB Storage Space    keyName: storage_snapshot_space
    ]
}

# Declares the API client
client = SoftLayer.Client()

try:
    # Use placeOrder method when you ready to order
    result = client['SoftLayer_Product_Order'].verifyOrder(orderTemplate)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. %s, %s" % (e.faultCode, e.faultString))

```

## **Complex example**

Following is a more complex example which order a file storage by setting only the parameters of location, size, and iops.

```python
import SoftLayer
import json

# Values "AMS01", "AMS03", "CHE01", "DAL05", "DAL06" "FRA02", "HKG02", "LON02", etc.
location = "AMS01"

# Values: "0.25", "2", "4"
iops = "2"

# Values "20", "40", "80", "100", etc.
storageSize = "20"

PACKAGE_ID = 240

client = SoftLayer.Client()

productOrderService = client['SoftLayer_Product_Order']
packageService = client['SoftLayer_Product_Package']
locationGroupService = client['SoftLayer_Location_Group_Pricing']
locationService = client['SoftLayer_Location']

objectFilterDatacenter = {"name": {"operation": location.lower()}}
objectFilterStorageEnterprise = {"items": {"categories": {"categoryCode": {"operation": "storage_service_enterprise"}}}}
objectFilterFileStorage = {"items": {"categories": {"categoryCode": {"operation": "storage_file"}}}}
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
            }
        ]
    }
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderData)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
```