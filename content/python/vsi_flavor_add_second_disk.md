---
title: "Add second disk on flavor vsi"
description: "Upgrade a flavor vsi in order to add a second disk"
date: "2018-08-09"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Item_Price"
tags:
    - "upgrade"
    - "virtualguest"    
---

The example retrieves the packageId and presetId whit which the device was ordered, change the presetId if you wants to add the second disk and upgrade the CPU, RAM, or First Disk.

```python

import SoftLayer
import json

class example():
    def __init__(self):        
        self.client = SoftLayer.Client()
        self.orderData = {}
    
    # Retrieve the packageId and presetId with which the device was ordered
    # and set them in the orderData
    def setPackageAndPreset(self, guestId):
        mask = "mask[id,orderItem[package,presetId]]"

        item = self.client['Virtual_Guest'].getBillingItem(id=guestId, mask=mask)
        
        self.orderData['packageId'] = item['orderItem']['package']['id']
        self.orderData['presetId'] = item['orderItem']['presetId']

    def addSecondDisk(self, guestId, priceId=None, note=None, date="NOW"):
        self.setPackageAndPreset(guestId)
        
        prices = [{
            'id': priceId,
            'categories': [{
                'categoryCode': 'guest_disk1',    #second disk
                'complexType': 'SoftLayer_Product_Item_Category'
            }],
            'complexType': 'SoftLayer_Product_Item_Price'
        }]

        # Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade object
        # containing the upgrade you wish to place.
        properties = [
            {
                'name': 'NOTE_GENERAL',
                'value': note
            },   
            {
                'name': 'MAINTENANCE_WINDOW',
                'value': date
            }
        ]

        self.orderData['virtualGuests'] = [{'id': guestId}]
        self.orderData['prices'] = prices
        self.orderData['properties'] = properties
        self.orderData['complexType'] = 'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade'
        
        try:
            """
            Use verifyOrder method to test that your upgrade is fine and
            when you are ready you can call the placeOrder method.
            """
            result = self.client['Product_Order'].verifyOrder(self.orderData)
            print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
        except SoftLayer.SoftLayerAPIError as e:
            """
            If there was an error returned from the SoftLayer API then bomb out with the
            error message.
            """
            print("Unable to upgrade VSI faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

if __name__ == "__main__":    
    # ID of virtual guest you want to add a second disk
    guestID = 58670025

    # The price id of disk you want to add as second disk. To get prices
    # you can call the SoftLayer_Virtual_Guest::getUpgradeItemPrices method
    priceID = 204661   # 100 GB (LOCAL)

    note = "adding second disk"
    date = "NOW"

    # Start the script
    main = example()
    
    main.addSecondDisk(guestID, priceId=priceID, note=note, date=date)    

```