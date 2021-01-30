---
title: "Verify items conflicts in ordering"
description: "Items conflicts in ordering"
date: "2019-03-19"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Item_Resource_Conflict"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "conflicts"
    - "item"
    - "placeorder"
    - "verifyorder"
---
This example goes over how to find items conflicts in ordering, e.g. antivirus Windows has a conflict with OS linux, https://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item/#conflicts


```python
import SoftLayer
from SoftLayer.managers import ordering
from pprint import pprint


class ItemsConflicts:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        # slcli order package-list --package_type BARE_METAL_CPU
        # Will get you available package keynames
        self.package_keyname = "DUAL_E52600_V4_4_DRIVES"
        self.complex_type = 'SoftLayer_Container_Product_Order_Hardware_Server'

    def order(self, dc):
        order_svc = self.client['Product_Order']

        order_items = self.itemKeynameList()

        extras = \
            {"hardware": [
                {"hostname": "testOrder1", "domain": "test.com"}
            ],
                "sshKeys": [87634],
                "tags": "server, test"}
        if not self.items_conflicts(order_items):
            server_order = self.getOrderObject(dc, order_items, extras, 1)
            verify = order_svc.verifyOrder(server_order)
            # verify = order_svc.placeOrder(server_order)
            pprint(verify)

    def getOrderObject(self, dc, items, extras, quantity=1):
        """Uses the ordering manager to build a order object"""
        om = ordering.OrderingManager(
            self.client)
        order = om.generate_order(
            self.package_keyname,
            dc,
            items,
            self.complex_type,
            False,
            None,
            extras,
            quantity)
        return order

    def itemKeynameList(self):
        """Builds a list of item keyNames needed to order"""

        required_items = [
            "BANDWIDTH_500_GB",
            "HARD_DRIVE_1_00_TB_SATA_2",
            "DISK_CONTROLLER_NONRAID",
            "MONITORING_HOST_PING",
            "NOTIFICATION_EMAIL_AND_TICKET",
            "OS_CENTOS_7_X_64_BIT",
            "1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS",
            "1_IP_ADDRESS",
            "1_IPV6_ADDRESS",
            "RAM_128_GB_DDR4_2133_ECC_REG",
            "REBOOT_KVM_OVER_IP",
            "AUTOMATED_NOTIFICATION",
            "INTEL_INTEL_XEON_E52690_V4_2_60",
            "UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT",

            # e.g. antivirus Windows has a conflict with OS linux.
            'MCAFEE_VIRUSSCAN_ANTIVIRUS_WINDOWS',
        ]

        return required_items

    def items_conflicts(self, order_item_keynames):
        """Verify if there are items conflicts in items to order"""

        om = ordering.OrderingManager(self.client)
        prices = om.get_price_id_list(self.package_keyname, order_item_keynames)
        package = om.get_package_by_key(self.package_keyname)
        all_item = self.client['SoftLayer_Product_Package'].getItems(
            id=package['id'],
            mask='mask[id, description, keyName, prices[id],conflicts]')

        order_items = [item for item in all_item for price in item['prices'] if price['id'] in prices]

        for order_item in order_items:
            for item_to_compare in order_items:
                if order_item['id'] != item_to_compare['id']:
                    for item_conflict in item_to_compare['conflicts']:
                        if order_item['id'] == item_conflict['resourceTableId']:
                            print(order_item['description'] + ", keyName: " + str(order_item['keyName']))
                            print('cannot be ordered with item')
                            print(item_to_compare['description'] + ", keyName: " + str(item_to_compare['keyName']))
                            return True
        return False


if __name__ == "__main__":
    main = ItemsConflicts()
    main.order('dal09')


```
