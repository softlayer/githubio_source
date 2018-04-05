---
title: "Ordering Vyatta Network Gateways"
description: "Ordering Vyattas"
date: "2018-04-05"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Gateway_Appliance_Cluster"
    - "SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance"
tags:
    - "order"
    - "vyatta"
    - "vlans"
    - "placeorder"
---

This example goes over how to order a Single or HA vyatta with a bunch of optional settings. More context around ordering can be found in  https://softlayer.github.io/python/orderBareMetal/ and  https://softlayer.github.io/python/ordering_slcli/

```python
import SoftLayer
from SoftLayer.managers import ordering
import sys
from  pprint import pprint as pp
import logging


logging.debug("Starting up")
# Requires softlayer-python 5.4.3+

class vyattaOrderer():

    def __init__(self):
        if SoftLayer.__version__ < 'v5.4.3':
            print("SoftLayer needs to be 5.4.3+, is currently %s" % SoftLayer.__version__)
        self.client = SoftLayer.Client()
        # slcli order package-list --package_type BARE_METAL_GATEWAY 
        # Will get you available package keynames
        self.package_keyname = "2U_NETWORK_GATEWAY_APPLIANCE_1O_GBPS"
        self.complex_type = 'SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance'


    def orderVyatta(self, dc, pub_vlan='', prv_vlan=''):
        """Actually orders a vyatts
            Required
                - dc
                - Server Chassis
                - RAM
                - OS (not really though)
                - HD (number, raid, partition)
                - Bandwidth 
                - Port Speed
                - IPv6
            Options
                - vlans
                - provision scrips
                - ssh keys
                - userdata
                - hostname, domain
        """
        
        order_svc = self.client['Product_Order']

        order_items = self.itemKeynameList()

        extras = {}
        extras['hardware'] = [
            self.generateHardwareEntry('vyatta1', 'test.com', pub_vlan, prv_vlan, 'vyatta1 Test')
        ]
        extras['storageGroups'] = [self.generateRaidEntry()]
        extras['sshKeys'] = [{'sshKeyIds': [87634]}]
        extras['provisionScripts'] = [
        'https://raw.githubusercontent.com/softlayer/softlayer.github.io/master/provision-test.sh'
        ]

        vyatta_order = self.getOrderObject(dc, order_items, extras, 1)
        order_object = {
            'orderContainers': [
                vyatta_order
            ]
        }

        verify = order_svc.verifyOrder(order_object)
        # verify = order_svc.placeOrder(order_object)
        pp(verify)
        print("done")

    def orderVyattaHA(self, dc, pub_vlan='', prv_vlan=''):
        order_svc = self.client['Product_Order']
        om = ordering.OrderingManager(self.client)

        order_items = self.itemKeynameList()

        extras = {}
        extras['hardware'] = [
            self.generateHardwareEntry('vyatta1', 'test.com', pub_vlan, prv_vlan, 'vyatta1 Test'),
            self.generateHardwareEntry('vyatta2', 'test.com', pub_vlan, prv_vlan, 'vyatta2 Test')
        ]
        extras['storageGroups'] = [self.generateRaidEntry()]
        mySshKey = 87634
        extras['sshKeys'] = [{'sshKeyIds': [mySshKey]}, {'sshKeyIds': [mySshKey]}]
        # Each server needs a provision script
        extras['provisionScripts'] = [
        'https://raw.githubusercontent.com/softlayer/softlayer.github.io/master/provision-test.sh',
        'https://raw.githubusercontent.com/softlayer/softlayer.github.io/master/provision-test.sh'
        ]
        extras['clusterIdentifier'] = 'myTestClusterOfVyattas'

        vyatta_order = self.getOrderObject(dc, order_items, extras, 2)

        cluster_extras = {
            'clusterIdentifier': 'myTestClusterOfVyattas',
            "sshKeys": [{"sshKeyIds": [mySshKey]}]
        }
        cluster_type = "SoftLayer_Container_Product_Order_Gateway_Appliance_Cluster"
        cluster_object = om.generate_order('NETWORK_GATEWAY_APPLIANCE_CLUSTER', dc, ['GATEWAY_APPLIANCE_CLUSTER'],
                                            cluster_type, False, None, cluster_extras, 1)
        # the cluster order object is a bit special, and we need to remove these for it to work properly
        del cluster_object['location']
        del cluster_object['useHourlyPricing']
        order_object = {
            'orderContainers': [
                vyatta_order,
                cluster_object
            ]
        }

        verify = order_svc.verifyOrder(order_object)
        # verify = order_svc.placeOrder(order_object)
        pp(verify)
        print("done")


    def generateHardwareEntry(self, hostname, domain, prv_vlan='', pub_vlan='', userData=''):
        hardware = {
            'domain': domain,
            'hostname': hostname,
            'primaryBackendNetworkComponent': 
                {'networkVlan': {'id' : int(pub_vlan)}},
            'primaryNetworkComponent': 
                {'networkVlan': {'id' : int(prv_vlan)}},
            'userData': [{'value': userData}]
        }
        return hardware

    def generateRaidEntry(self):
        storage = {
                'arrayTypeId': 2,
                'hardDrives': [0,1],
                'partitionTemplateId': 1
        }
        return storage

    def getOrderObject(self, dc, items, extras, quantity = 1):
        """Uses the ordering manager to build a order object"""
        om = ordering.OrderingManager(self.client)
        order = om.generate_order(self.package_keyname, dc, items, self.complex_type, False, None, extras, quantity)
        # pp(order)
        return order



    def datacenterList(self):
        """Prints a list of dcs and their ids"""
        om = ordering.OrderingManager(self.client)
        locations = om.package_locations(self.package_keyname)
        print("ID, name, longName")
        for region in locations:
            for location in region['locations']:
                if location['locationPackageDetails'][0]['isAvailable'] == 1:
                    dc = location['location']
                    print("%s, %s, %s" % (dc['id'], dc['name'], dc['longName']))


    def itemKeynameList(self):
        """Builds a list of item keyNames needed to order a VYATTA

        To see what category of items are required, use this command
        $> slcli order category-list 2U_NETWORK_GATEWAY_APPLIANCE_1O_GBPS
        
        To see what items are in each category, use this command
        $> slcli order item-list 2U_NETWORK_GATEWAY_APPLIANCE_1O_GBPS
        
        Price Ids are subject to change, so please use keynames to get price ids
        at order time.
        """

        # The junk all orders have to have
        required_items = [
            'AUTOMATED_NOTIFICATION',
            'MONITORING_HOST_PING',
            'NOTIFICATION_EMAIL_AND_TICKET',
            'REBOOT_KVM_OVER_IP',
            'NESSUS_VULNERABILITY_ASSESSMENT_REPORTING',
            'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT',
            'REDUNDANT_POWER_SUPPLY',
        ]

        # 20000GB is recommended. 
        # BANDWIDTH_0_GB_2 and BANDWIDTH_UNLIMITED_100_MBPS_UPLINK are also possible
        network_items = [
            'BANDWIDTH_20000_GB',
            '10_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS',
            '1_IP_ADDRESS',
            '1_IPV6_ADDRESS' 
        ]

        # Were going to go with RAID1, 500GB. 
        hard_drive = [
            'HARD_DRIVE_500GB_SATA_II',
            'HARD_DRIVE_500GB_SATA_II',
            'DISK_CONTROLLER_RAID_1'
        ]

        ram = [
            # 'RAM_16_GB_DDR3_1333_ECC_REG'
            'RAM_32_GB_DDR3_1333_REG_2',
            # 'RAM_64_GB_DDR3_1333_REG_2'
            # 'RAM_48_GB_DDR3_1333_REG'
            # 'RAM_96_GB_DDR3_1333_REG'
            # 'RAM_128_GB_DDR3_1333_REG_2'
            # 'RAM_256_GB_DDR3_1333_REG_2'
        ]

        # Sets the server chassis and OS
        server = [
            'OS_VYATTA_5600_5_X_UP_TO_20GBPS_SUBSCRIPTION_EDITION_64_BIT',
            'INTEL_XEON_2620_2_40',
            # 'INTEL_INTEL_XEON_E52620_V4_2_10'
            # 'INTEL_XEON_2650_2_30'
            # 'INTEL_INTEL_XEON_E52650_V4_2_20'
            # 'INTEL_XEON_2690_2_60'
            # 'INTEL_INTEL_XEON_E52690_V4_2_60'
        ]

        allItems = required_items + network_items + hard_drive + ram + server
        return allItems

    def listAvailableVlans(self, dc_id):
        """Will find available VLANs that a vyatta can be ordered on"""

        mask = """mask[
            network, type, primaryRouter[datacenter], 
            attachedNetworkGatewayFlag, dedicatedFirewallFlag
        ]"""

        _filter = {
            'networkVlans' : {
                'primaryRouter': {
                    'datacenter' : { 'id': {'operation': dc_id} }
                }
            }
        }
        result = self.client['SoftLayer_Account'].getNetworkVlans(mask=mask,filter=_filter)

        # Vlans that are not-standard, part of a firewall or gateway, can't be ordered on. 
        print("ID, Vlan Number, Type, Router")
        for vlan in result:
            vlan_type = vlan['type']['keyName']
            if vlan_type == 'GATEWAY':
                vlan_type = 'GATEWAY (No ordering)'
            elif vlan['dedicatedFirewallFlag'] == 1:
                vlan_type = "%s/FIREWALL (No ordering)" % vlan_type
            elif vlan['attachedNetworkGatewayFlag']:
                vlan_type = "%s/GATEWAY MEMBER (No ordering)" % vlan_type

            print("%s - VLAN: %s - Type: %s - %s " % 
                (vlan['id'], 
                 vlan['vlanNumber'],
                 vlan_type, 
                 vlan['primaryRouter']['hostname'])
            )


if __name__ == "__main__":
    main = vyattaOrderer()
    # 2255245 - VLAN: 946 - Type: STANDARD - bcr01a.sjc04
    # 2255243 - VLAN: 913 - Type: STANDARD - fcr01a.sjc04
    # main.orderVyatta('sjc04', 2255243, 2255245)
    main.orderVyattaHA('sjc04', 2255243, 2255245)

```