---
title: "order_evault.py"
description: "order_evault.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault"
    - "SoftLayer_Hardware_Server"
tags:
    - "evault"
---


```
"""
Order a Evault device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/services/SoftLayer_Location
http://sldn.softlayer.com/reference/services/SoftLayer_Location/getDatacenters
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/blog/cmporter/Location-based-Pricing-and-You
http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-3
http://sldn.softlayer.com/article/Object-Filters
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
location = "DAL05"

# Values "20", "30", "40", "50", "60", "100", etc.
size = "20"

# The VSI or Sever IP address where the Evault will be added.
ip = "108.168.251.167"

PACKAGE_ID = 0

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']
packageService = client['SoftLayer_Product_Package']
locationService = client['SoftLayer_Location']
serverService = client['SoftLayer_Hardware_Server']
vsiService = client['SoftLayer_Virtual_Guest']

objectFilterDatacenter = {"name": {"operation": location.lower()}}
objectMaskLocation = "mask[priceGroups]"

try:
    # Getting the datacenter.
    datacenter = locationService.getDatacenters(filter=objectFilterDatacenter, mask=objectMaskLocation)
    objectFilterEvaultPrices = {}
    if len(datacenter[0]['priceGroups']) == 0:
        objectFilterEvaultPrices = {"itemPrices": {"item": {"capacity": {"operation": size}}, "categories": {"categoryCode": {"operation": "evault"}}, "locationGroupId": {"operation": "is null"}}}
    else:
        objectFilterEvaultPrices = {"itemPrices": {"item": {"capacity": {"operation": size}}, "categories": {"categoryCode": {"operation": "evault"}}, "locationGroupId": {"operation": datacenter[0]['priceGroups'][0]['id']}}}
    # Getting the Evault prices.
    prices = packageService.getItemPrices(id=PACKAGE_ID, filter=objectFilterEvaultPrices)
    # In case we get an empty list of prices the reason could be that there is no a specific price for the selected location so we try looking an standard price.
    if len(prices) == 0:
        objectFilterEvaultPrices = {"itemPrices": {"item": {"capacity": {"operation": size}}, "categories": {"categoryCode": {"operation": "evault"}}, "locationGroupId": {"operation": "is null"}}}
        prices = packageService.getItemPrices(id=PACKAGE_ID, filter=objectFilterEvaultPrices)
    # In case the list of prices is still empty that means that the configured size is invalid for an Evault.
    if len(prices) == 0:
        print("The configured size: " + size + " is not valid for an Evault device.")
        exit(1)

    # Build the order template
    orderTemplate = {
        "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault",
        "location": datacenter[0]['id'],
        "packageId": PACKAGE_ID,
        "prices": [
            {
                "complexType": "SoftLayer_Product_Item_Price",
                "id": prices[0]['id']
            }
        ],
        "quantity": 1
    }
    # Getting the device id.
    # We look for the IP address in the servers.
    device = serverService.findByIpAddress(ip)
    if 'id' in device:
        # Adding the server id to the order template.
        orderTemplate['hardware'] = []
        hardware = {}
        hardware['id'] = device['id']
        orderTemplate['hardware'].append(hardware)
    else:
        # We look for the IP address in the VSIs.
        device = vsiService.findByIpAddress(ip)
        if 'id' not in device:
            print("The configured IP address: " + ip + " does not exist.")
            exit(1)
        # Adding the VSI to the order
        orderTemplate['virtualGuests'] = []
        vsi = {}
        vsi['id'] = device['id']
        orderTemplate['virtualGuests'].append(vsi)
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderTemplate)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
