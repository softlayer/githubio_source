---
title: "Order a performance storage (block/file)"
description: "Shows how to order performance storage devices"
date: "2018-11-22"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs"
tags:
    - "order"
    - "storage"    
    - "performance"
---

### **Important Note:** There is a new version of storage devices (STaaS v2) so it is recomended to review [Order Block/File storages with Managers](../order_block_file_storage_with_managers)

Performance Block/File storage devices are under package 222 and they are differentiated by the `complexType` in the order template, being `SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi` for Block and `SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs` for File storages.

These storage devices do not support snapshots, there is not any category name called `storage_snapshot_space` or similar in the package configuration, you can execute the following code to verify this last.

```python
import SoftLayer
from pprint import pprint

client = SoftLayer.Client()
packageService = client['SoftLayer_Product_Package']

result = packageService.getConfiguration(id=222, mask="itemCategory")
pprint(result)
```
<br />

**Tips before ordering**

In most of the cases the order verification fails whether the selected price cannot be ordered in the selected location or it does not meet the capacity restriction of the storage space.

Following REST call retrieves all prices under package 240 and shows on which locations are available, if `locationGroupId` is null means the price is standard and can be used on any location.

```html
https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/222/getItemPrices?objectMask=mask[id,capacityRestrictionMaximum,capacityRestrictionMinimum,capacityRestrictionType,locationGroupId,item[capacity,description],categories,pricingLocationGroup[locations]]
```

About capacity restrictions, the `performance_storage_iops` items have capacity restrictions (min/max) which should match with the `capacity` value of the selected `performance_storage_space` item, it means if you want an storage space of "40 GB Storage Space" and "600 IOPS":

```json
    {
        "id": 40692,
        "locationGroupId": null,
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
            "capacity": "40",
            "description": "40 GB Storage Space"
        }
    }
```

Then price of `performance_storage_iops` should be:

```json
    {
        "id": 40942,
        "locationGroupId": null,
        "capacityRestrictionMaximum": "40",
        "capacityRestrictionMinimum": "40",
        "capacityRestrictionType": "STORAGE_SPACE",
        "categories": [
            {
                "categoryCode": "performance_storage_iops",
                "id": 384,
                "name": "Performance Storage IOPS",
                "quantityLimit": 0,
                "sortOrder": null
            }
        ],
        "item": {
            "capacity": "600",
            "description": "600 IOPS"
        }
    }
```

## **Block Performance Storage**

```python
import SoftLayer
from pprint import pprint

orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi",
    "location": "DALLAS05",
    "quantity": 1,
    "packageId": 222,
    # To see the list of prices available for the package
    # use the SoftLayer_Product_Package::getItems method with masks
    # or SoftLayer_Product_Package::getItemPrices
    "prices": [
        {"id": 40672},      # BlockStorage(Performance) keyName: performance_storage_iscsi
        {"id": 40692},      # 40GB Storage Space        keyName: performance_storage_space
        {"id": 40942}       # 600 IOPS                  keyName: performance_storage_iops
    ],
    "osFormatType": {"keyName": "LINUX"}
}

# Declares the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client()
productOrderService = client['SoftLayer_Product_Order']

try:
    # Use placeOrder method when you ready to order
    result = productOrderService.verifyOrder(orderTemplate)
    pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. %s, %s" % (e.faultCode, e.faultString))
```

## **File Performance Storage**

Since the prices are the same, basically it is only to required change the price of `performance_storage_iscsi` by `performance_storage_nfs`, and remove the property `osFormatType`

```python
import SoftLayer
from pprint import pprint

orderTemplate = {
    'complexType': 'SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs',
    'quantity': 1,
    'packageId': 222,
    'location': 'DALLAS09',
    # To see the list of prices available for the package
    # use the SoftLayer_Product_Package::getItems method with masks
    # or SoftLayer_Product_Package::getItemPrices
    'prices': [
        {'id': 40662},  # File Storage (Performance)    keyName: performance_storage_nfs
        {'id': 40692},  # 40GB Storage Space            keyName: performance_storage_space
        {'id': 40942}   # 600 IOPS                      keyName: performance_storage_iops
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

Following is a more complex example which order a block storage by setting only the parameters of location, size, iops, and os.

```python
import SoftLayer
import json

# Values "AMS01", "AMS03", "CHE01", "DAL05", "DAL06" "FRA02", "HKG02", "LON02", etc.
location = "AMS01"

# Values "20", "40", "80", "100", etc.
storageSize = "40"

# Values between "100" and "6000" by intervals of 100.
iops = "100"

# Values "Hyper-V", "Linux", "VMWare", "Windows 2008+", "Windows GPT", "Windows 2003", "Xen"
os = "Linux"

PACKAGE_ID = 222

client = SoftLayer.Client()
productOrderService = client['SoftLayer_Product_Order']
packageService = client['SoftLayer_Product_Package']
locationService = client['SoftLayer_Location']
osService = client['SoftLayer_Network_Storage_Iscsi_OS_Type']

objectFilterDatacenter = {"name": {"operation": location.lower()}}
objectFilterStorageNfs = {"items": {"categories": {"categoryCode": {"operation": "performance_storage_iscsi"}}}}
objectFilterOsType = {"name": {"operation": os}}

try:
    # Getting the datacenter.
    datacenter = locationService.getDatacenters(filter=objectFilterDatacenter)
    # Getting the performance storage NFS prices.
    itemsStorageNfs = packageService.getItems(id=PACKAGE_ID, filter=objectFilterStorageNfs)
    # Getting the storage space prices
    objectFilter = {
        "itemPrices": {
            "item": {
                "capacity": {
                    "operation": storageSize
                }
            },
            "categories": {
                "categoryCode": {
                    "operation": "performance_storage_space"
                }
            },
            "locationGroupId": {
                "operation": "is null"
            }
        }
    }
    pricesStorageSpace = packageService.getItemPrices(id=PACKAGE_ID, filter=objectFilter)
    # If the prices list is empty that means that the storage space value is invalid.
    if len(pricesStorageSpace) == 0:
        raise ValueError('The storage space value: ' + storageSize + ' GB, is not valid.')
    # Getting the IOPS prices
    objectFilter = {
        "itemPrices": {
            "item": {
                "capacity": {
                    "operation": iops
                }
            },
            "attributes": {
                "value": {
                    "operation": storageSize
                }
            },
            "categories": {
                "categoryCode": {
                    "operation": "performance_storage_iops"
                }
            },
            "locationGroupId": {
                "operation": "is null"
            }
        }
    }
    pricesIops = packageService.getItemPrices(id=PACKAGE_ID, filter=objectFilter)
    # If the prices list is empty that means that the IOPS value is invalid for the configured storage space.
    if len(pricesIops) == 0:
        raise ValueError('The IOPS value: ' + iops + ', is not valid for the storage space: ' + storageSize + ' GB.')
    # Getting the OS.
    os = osService.getAllObjects(filter=objectFilterOsType)
    # Building the order template.
    orderData = {
        "complexType": "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi",
        "packageId": PACKAGE_ID,
        "location": datacenter[0]['id'],
        "quantity": 1,
        "prices": [
            {
                "id": itemsStorageNfs[0]['prices'][0]['id']
            },
            {
                "id": pricesStorageSpace[0]['id']
            },
            {
                "id": pricesIops[0]['id']
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