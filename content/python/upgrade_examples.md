---
title: "Upgrade Hardware and Virtual Servers"
description: "A few examples on how to find upgrade prices, actually do the upgrade with a maintenance window, and verify everything."
date: "2016-03-22"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Product_Order_Hardware_Server_Upgrade"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
    - "SoftLayer_Product_Order"
tags:
    - "placeOrder"
    - "verifyOrder"
    - "upgrade"
    - "MAINTENANCE_WINDOW"
---

```
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    """
    Prints out what can be upgraded on a server by category.
    """
    def getUpgradeItemPrices(self, hardware_id, service='SoftLayer_Hardware_Server'):
        result = self.client[service].getUpgradeItemPrices(id=hardware_id)
        last_id = 0
        for item in result:
            now_id = item['categories'][0]['id']
            if now_id != last_id:
                print("%s (%s)" % (item['categories'][0]['name'], item['categories'][0]['id']))
            last_id = now_id
            print("\t %s (%s)" % (item['item']['description'], item['id']))


    """
    Get the available maintenance windows that exist for a server.
    "now" is still always an option
    """
    def getUpgradeTimes(self, hardware_id, beginDate, endDate):
        # getLocation doesn't return an id that is useful for getMaintenanceWindows
        # Needs to be the datacenter ID, not the location id...
        _mask = "mask[datacenter]"
        server = self.client['SoftLayer_Hardware_Server'].getObject(id=hardware_id,mask=_mask)
        pp(server)
        location_id = server['datacenter']['id']
        provision_service = self.client['SoftLayer_Provisioning_Maintenance_Window']
        windows = provision_service.getMaintenanceWindows(beginDate, endDate, location_id, 1)
        pp(windows)


    """
    Upgrades the network speed 1Gbps (price id = 274)
    MAINTENANCE_WINDOW requires both the time, AND the id of the maintenance window. Virtual Server upgrades do not require the ID, just bare metal.
    """
    def upgradeServer(self, hardware_id, place_order=False):
        product_client = self.client['SoftLayer_Product_Order']
        upgrade = {
            'complexType' : 'SoftLayer_Container_Product_Order_Hardware_Server_Upgrade',
            'hardware' : [{'id' : hardware_id}],
            'properties' : [
                {
                    'name' : 'MAINTENANCE_WINDOW', 
                    'value' : '2016-03-30T00:00:00-06:00'
                },
                {
                    'name' : 'MAINTENANCE_WINDOW_ID', 
                    'value' : 7
                }
            ],
            'prices': [{'id' : 274}]
        }
        pp(upgrade)
        print("Verifying Order....")
        result = product_client.verifyOrder(upgrade)
        pp(result)
        if place_order:
            print("PLACING ORDER....")
            place_result = product_client.placeOrder(upgrade)
            pp(place_result)


    """
    Adds a 10G disk (price id = 2255) to the second (id=82) and third (id=92)
    disk slots on the VSI. The price for both is the same, you just need to specify
    the propery category for each disk.
    """
    def upgradeVSI(self, vsi_id, place_order=False):
        product_client = self.client['SoftLayer_Product_Order']
        upgrade = {
            'complexType' : 'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade',
            'virtualGuests' : [{'id' : vsi_id}],
            'properties' : [
                {
                    'name' : 'MAINTENANCE_WINDOW', 
                    'value' : '2016-03-23 16:00:00'
                }
            ],
            'prices': [
                {
                    'categories' : [{'id' : 82}],
                    'id' : 2255
                },
                {
                    'categories' : [{'id' : 92}],
                    'id' : 2255
                }
            ]
        }
        pp(upgrade)
        print("Verifying Order....")
        result = product_client.verifyOrder(upgrade)
        pp(result)
        if place_order:
            print("PLACING ORDER....")
            place_result = product_client.placeOrder(upgrade)
            pp(place_result)


    """
    Gets some information about any current upgrade requests for a server
    """
    def getUpgradeInfo(self, hardware_id, service='SoftLayer_Hardware_Server'):
        result = self.client[service].getUpgradeRequest(id=hardware_id)
        pp(result)

if __name__ == "__main__":
    main = example()
    server_id = 662657
    # main.getUpgradeItemPrices(server_id)
    # main.getUpgradeTimes(server_id, '2016-03-30 00:00:00', '2016-03-31 20:00:00')
    # main.upgradeServer(server_id, True)
    vsi_id = 13106845
    # main.getUpgradeItemPrices(vsi_id,'SoftLayer_Virtual_Guest')
    # main.upgradeVSI(vsi_id, True)
    main.getUpgradeInfo(vsi_id,'SoftLayer_Virtual_Guest' )
```

