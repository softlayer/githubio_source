---
title: "Advanced Bare Metal Server Ordering"
description: "Explains how to build a bare metal order, includes how to get packages, prices (including pcie and gpu items), raid setup and vlans"
date: "2019-03-20"
classes:
    - "SoftLayer_Product_Order"
    - "SoftLayer_Configuration_Storage_Group_Array_Type"
    - "SoftLayer_Product_Package"
tags:
    - "order"
    - "vlan"
    - "baremetalservers"
    - "create"
    - "filter"
    - "hardware"
    - "objectfilter"
    - "packages"
    - "pricing"
    - "raid"
---


Example of how to build an order for a bare metal server. 

1. Find the package that you want to order. listServerPackages() will filter out all that are not bare metal servers
2. Use getServerPrices() to find the item keyNames you want to include in your order. These price IDs can be included prices array directly, but I've included gatherPriceIds() to match up KeyNames to build a list of price ids. getServerPrices() will also show the locations available for ordering.
3. listAvailableVlans() if you want to place the server on a specific VLAN. 
4. listPartitionTemplates() will show what partition schemes you can apply to a disk.
5. listRaidArrayTypes() shows what id numbers are for each RAID type.
6. Custom partitions can ONLY be specified for CentOS or RHEL servers, and ONLY on the secondary drives [^1]. Trying to do the same for the primary controller will result in the default partitinoTemplate being applied. Custom partitions also require the arraySize be declared.


```python
"""
@author Christopher Gallo
Places an order for a Bare Metal Server
"""
import SoftLayer
from pprint import pprint as pp
from prettytable import PrettyTable


class Ordering:

    def __init__(self):

        self.client = SoftLayer.create_client_from_env()

    def main(self, package_id, location_id, pub_vlan_id='', priv_vlan_id=''):
        """
        Places an order for a Bare Metal Instance
        """

        """These items are required for all servers and have a 0$ cost, some can be upgraded"""
        required_items = [
            'AUTOMATED_NOTIFICATION',
            'MONITORING_HOST_PING',
            'NOTIFICATION_EMAIL_AND_TICKET',
            'REBOOT_KVM_OVER_IP',
            'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT',
            'REDUNDANT_POWER_SUPPLY',
        ]
        """We need bandwidth, at least 1 ip, and the port speed """
        network_items = [
            'BANDWIDTH_500_GB',
            '1_IP_ADDRESS',
            '1_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED',
        ]
        """A disk controller, a duplicate entry for each disk you want, in order, ram, OS and processor chip """
        physical_items = [
            'DISK_CONTROLLER_RAID',
            'HARD_DRIVE_2_00_TB_SATA_2',
            'HARD_DRIVE_2_00_TB_SATA_2',
            'HARD_DRIVE_2_00_TB_SATA_2',
            'HARD_DRIVE_2_00_TB_SATA_2',
            'RAM_64_GB_DDR4_2133_ECC_NON_REG',
            # 'OS_CENTOS_7_X_64_BIT',
            'OS_WINDOWS_2012_FULL_STD_64_BIT',
            'INTEL_INTEL_XEON_E52620_V4_2_10',
            'HARD_DRIVE_NVME_375_GB_PCIE',  # PCIe component slot0
            'HARD_DRIVE_NVME_375_GB_PCIE'  # PCIe component slot1
        ]

        all_items = required_items + network_items + physical_items
        prices = self.gatherPriceIds(package_id, all_items)
        productOrder = {'orderContainers': [
            {'hardware':
                [
                    {
                        'domain': u'cgallo.com',
                        'hostname': u'vmware-testing01',
                        'primaryBackendNetworkComponent': {'networkVlan': {'id': int(priv_vlan_id)}},
                        'primaryNetworkComponent': {'networkVlan': {'id': int(pub_vlan_id)}}
                    }
                ],
                'location': location_id,
                'packageId': package_id,
                'prices': prices,
                'quantity': 1,
                'storageGroups': [
                    {
                        'arrayTypeId': 2,
                        'arraySize': 2000,
                        'hardDrives': [0, 1],
                        'partitionTemplateId': 1
                    },
                    {
                        'arrayTypeId': 9,
                        'arraySize': 2000,
                        'hardDrives': [2],
                        # Defining partitions on secondary storage groups is only allowed for CentOS
                        # and Red Hat operating systems.
                        # 'partitions': [
                        #     {'name': '/', 'size': 200, 'isGrow': 0},
                        #     {'name': '/boot', 'size': 100},
                        #     {'name': '/usr', 'size': 200},
                        #     {'name': '/mine', 'size': 200},
                        #     {'name': '/media', 'size': 1, 'isGrow': 1},
                        # ]

                    },
                    {
                        'arrayTypeId': 9,
                        'arraySize': 2000,
                        'hardDrives': [3]
                    }
                ],
            }
        ]
        }
        pp(productOrder)
        order = self.client['Product_Order'].verifyOrder(productOrder)
        # order = self.client['Product_Order'].placeOrder(productOrder)
        pp(order)

    def listServerPackages(self):
        mask = "mask[type]"
        _filter = {
            'type': {
                'keyName': {'operation': 'BARE_METAL_CPU'},
            },
        }
        result = self.client['Product_Package'].getAllObjects(mask=mask, filter=_filter)
        table = PrettyTable()
        table.title = "Server Packages"
        table.field_names = ["id", "name", "keyName", "type"]

        for product in result:
            table.add_row([product['id'],
                           product['name'],
                           product['keyName'],
                           product['type']['keyName']]
                          )
        print(table)

    def listPartitionTemplates(self):
        mask = "mask[partitionTemplates[data]]"
        result = self.client['SoftLayer_Hardware_Component_Partition_OperatingSystem'].getAllObjects(mask=mask)
        print("OS Type, Notes")
        table = PrettyTable()
        table.title = "Partition Templates"
        table.field_names = ["OS Type - Notes"]
        for os_type in result:
            table_os = PrettyTable()
            table_os.title = "{} - {}".format(os_type['description'], os_type['notes'])
            table_os.field_names = ["Template id", "Description"]
            for template in os_type['partitionTemplates']:
                template_data = []
                table_partition = PrettyTable()
                table_partition.field_names = [template['description']]
                table_partition.align[template['description']] = "l"
                for partition in template['data']:
                    template_data.append("{} - {} {}"
                                         .format(partition['partitionName'],
                                                 partition['partitionSize'],
                                                 'Grow' if partition['isGrow'] else ''))
                table_partition.add_row(['\n'.join(template_data)])
                table_os.add_row([template['id'], table_partition])
            table.add_row([table_os])

        print(table)

    def listRaidArrayTypes(self):
        result = self.client['SoftLayer_Configuration_Storage_Group_Array_Type'].getAllObjects()
        table = PrettyTable()
        table.title = "Raid Array Types"
        table.field_names = ["id", "keyName", "description", "Min", 'Max']
        for raid in result:
            table.add_row([raid['id'],
                           raid['keyName'],
                           raid['description'],
                           raid['minimumDrives'],
                           raid['maximumDrives']]
                          )
        print(table)

    def listAvailableVlans(self, dc_id):
        mask = "mask[network,type,primaryRouter[datacenter]]"
        _filter = {
            'networkVlans': {
                'primaryRouter': {
                    'datacenter': {'id': {'operation': dc_id}}
                }
            }
        }
        result = self.client['SoftLayer_Account'].getNetworkVlans(mask=mask, filter=_filter)
        table = PrettyTable()
        table.title = "Available Vlans"
        table.field_names = ["id", "VLAN", "type", "primaryRouter"]
        for vlan in result:
            table.add_row([vlan['id'],
                           vlan['vlanNumber'],
                           vlan['type']['keyName'],
                           vlan['primaryRouter']['hostname']]
                          )
        print(table)

    def getServerPrices(self, package_id):
        mask = "mask[regions,items[prices],activeServerItems[prices]]"
        # locations = self.client['Product_Package'].getLocations(id=package_id)
        result = self.client['Product_Package'].getObject(mask=mask, id=package_id)

        table = PrettyTable()
        table.title = "Locations"
        table.field_names = ["Location ID", "Location Name"]
        for location in result['regions']:
            table.add_row([location['location']['location']['id'], location['description']])
        print(table)

        table = PrettyTable()
        table.title = "Items Prices"
        table.field_names = ["Price ID", "description", "cores", "Monthly Fee", "KeyName"]
        for item in result['items']:
            for prices in item['prices']:
                # only print the Default location price.
                # The ordering system will replace the default price id for you if ordering in a non-usa region.
                if prices['locationGroupId'] is None:
                    # Some software has core restrictions that effect prices
                    if 'capacityRestrictionType' in prices:
                        cores = "%s - %s" % (
                            prices['capacityRestrictionMinimum'],
                            prices['capacityRestrictionMaximum'])
                        table.add_row([prices['id'],
                                       str(item['description']).replace(" - ", "\n"),
                                       cores, prices.get('recurringFee', '?'),
                                       item['keyName']])

                    else:
                        table.add_row([prices['id'],
                                       str(item['description']).replace(" - ", "\n"),
                                       "", prices.get('recurringFee', '?'),
                                       item['keyName']])
        print(table)

        # serverItems = self.client['Product_Package'].getActiveServerItems(id=package_id)
        table = PrettyTable()
        table.title = "SERVER ITEMS"
        table.field_names = ["Price ID", "description", "Monthly Fee", "KeyName"]
        for item in result['activeServerItems']:
            for prices in item['prices']:
                # only print the Default location price.
                # The ordering system will replace the default price id for you if ordering in a non-usa region.
                if prices['locationGroupId'] is None:
                    table.add_row([prices['id'],
                                   str(item['description']).replace(" - ", "\n"),
                                   prices.get('recurringFee', '?'),
                                   item['keyName']])
        print(table)

    def gatherPriceIds(self, package_id, keyNames):
        # This will work for prices that have core requirements
        mask = 'mask[id,itemCategory,keyName,prices[categories],' \
               'capacityRestrictedProductFlag,totalPhysicalCoreCapacity]'
        items = self.client['Product_Package'].getItems(mask=mask, id=package_id)

        items_restricted_by_capacity = [item for item in items if item['capacityRestrictedProductFlag'] is True]

        prices = []
        category_dict = {"gpu0": -1, "pcie_slot0": -1}
        core_capacity = 0

        for item_keyname in keyNames:
            try:
                matching_item = [i for i in items if i['keyName'] == item_keyname][0]
            except IndexError:
                raise SoftLayer.SoftLayerError(
                    "Item {} does not exist for package {}".format(item_keyname,
                                                                   package_id))
            item_category = matching_item['itemCategory']['categoryCode']
            if item_category == 'server':
                core_capacity = int(matching_item['totalPhysicalCoreCapacity'])
                break

        for item_keyname in keyNames:
            try:
                matching_item = [i for i in items if i['keyName'] == item_keyname][0]
            except IndexError:
                raise SoftLayer.SoftLayerError(
                    "Item {} does not exist for package {}".format(item_keyname,
                                                                   package_id))

            item_category = matching_item['itemCategory']['categoryCode']

            if item_category not in category_dict:

                if matching_item in items_restricted_by_capacity:
                    price_id = [p['id'] for p in matching_item['prices']
                                if not p['locationGroupId']
                                and core_capacity <= int(p['capacityRestrictionMaximum'])][0]

                else:
                    price_id = [p['id'] for p in matching_item['prices']
                                if not p['locationGroupId']][0]

            else:
                category_dict[item_category] += 1
                category_code = item_category[:-1] + str(category_dict[item_category])
                price_id = [p['id'] for p in matching_item['prices']
                            if not p['locationGroupId']
                            and p['categories'][0]['categoryCode'] == category_code][0]

            prices.append({"id": price_id})

        return prices


if __name__ == "__main__":
    main = Ordering()

    """
    Step 1, find the processor type you want    
    553  Dual E5-2600 v4 Series (12 Drives)  DUAL_E52600_V4_12_DRIVES  BARE_METAL_CPU
    """
    # main.listServerPackages()
    package_id = 553

    """
    Step 2, collect all the pieces you want to order
    getServerPrices will list out all the keyNames and cost of components
    that can be ordered on a certain package. Will also list the DCs that this
    server is available in.
    """
    main.getServerPrices(package_id)
    location_id = 814994  # "AMSTERDAM03"

    """
    Step 3, customize and place the order
    """
    main.listAvailableVlans(location_id)
    pub_vlan_id = 2439425
    priv_vlan_id = 2207425
    # main.listPartitionTemplates()
    main.listRaidArrayTypes()
    main.main(package_id, location_id, pub_vlan_id, priv_vlan_id)
```


## Exceptions you might see
* SoftLayerAPIError(SoftLayer_Exception_Order_InvalidStorageGroups): 

> Defining partitions on secondary storage groups is only allowed for CentOS and Red Hat operating systems.

>>Chose the right operating system.

* SoftLayerAPIError(SoftLayer_Exception_Order_InvalidLocation): 

> The location provided for this order is invalid.

>>Choose a correct location, locations should be displayed in getServerPrices()

* SoftLayerAPIError(SoftLayer_Exception_Order_InvalidStorageGroups): 

> Storage group #1 does not have a grow partition. Each storage group with partitions defined must have a grow partition.

>>Make sure your partition has 'isGrow' = 1 at some point.

* SoftLayerAPIError(SoftLayer_Exception_Order_InvalidStorageGroups): 

> Storage group #1 with size (GB) is smaller than the total partitioned size (501GB).

>>You forgot to assign an arraySize. 



## Another Example
>This is an older example that hard codes priceIds, which can be a bad practice as priceIds can change without notice.

```python
import SoftLayer
import json

quantity = 1
location = 'AMSTERDAM'
packageId = 259
lvmFlag = True
# Building a skeleton SoftLayer_Hardware_Server object to model the hostname and
# domain we want for our server. If you set quantity greater then 1 then you
# need to define one hostname/domain pair per server you wish to order.
hardware = [
    {
        'hostname': 'test',
        'domain': 'example.org'
    }
]

# Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.
# Every item in SoftLayer's product catalog is assigned an id. Use these ids
# to tell the SoftLayer API which options you want in your new server. Use
# the getActivePackages() method in the SoftLayer_Account API service to get
# a list of available item and price options per available package.
prices = [
    {'id': 179861},  # server: Single  Intel  Xeon  E5-2620 (6 Cores, 2.00 GHz)
    {'id': 76165},  # ram: 8 GB RAM
    {'id': 44988},  # os: CentOS 7.x (64 bit)
    {'id': 74995},  # disk_controller: RAID
    {'id': 64769},  # disk0: 2.00 TB SATA
    {'id': 69535},  # disk1: 500 GB SATA
    {'id': 69535},  # disk2: 500 GB SATA
    {'id': 50357},  # bandwidth: 500 GB Bandwidth
    {'id': 273},  # port_speed: 100 Mbps Public & Private Network Uplinks
    {'id': 55},  # monitoring: Host Ping
    {'id': 58},  # response: Automated Notification
    {'id': 420},  # vpn_management: Unlimited SSL VPN Users & 1 PPTP VPN User per account
    {'id': 418},  # vulnerability_scanner: Nessus Vulnerability Assessment & Reporting
    {'id': 21},  # pri_ip_addresses: 1 IP Address
    {'id': 57},  # notification: Email and Ticket
    {'id': 906}  # remote_management: Reboot / KVM over IP
]

# Building a skeleton SoftLayer_Container_Product_Order_Storage_Group object
# Storage groups will only be used if the 'RAID' disk controller price is selected.
# Any other disk controller types will ignore the storage groups set here.
# The first storage group in this array will be considered the primary storage group,
# which is used for the OS. Any other storage groups will act as data storage.
storageGroups = [
    {
         "arraySize": 1000,
         "arrayTypeId": 3,  # RAID_5
         "hardDrives": [
            0,
            1,
            2
         ],
         "partitionTemplateId": 6
     },
    {
         "arraySize": 500,
         "arrayTypeId": 9,
         "hardDrives": [
             0
         ],
         # The custom partitions only work on other storage groups
         # different from the primary one
         "partitions": [
             {
                 "isGrow": False,
                 "name": "/test",
                 "size": 100
             },
             {
                 "isGrow": True,
                 "name": "/test2",
                 "size": 200
             }
         ]
     },
]

# Building a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
# containing the order you wish to place.
orderTemplate = {
    'quantity': quantity,
    'location': location,
    'packageId': packageId,
    'prices': prices,
    'hardware': hardware,
    'storageGroups': storageGroups,
    'lvmFlag': lvmFlag
}

# Creating a SoftLayer API client object
client = SoftLayer.create_client_from_env()
# verifyOrder() will check your order for errors. Replace this with a call
# to placeOrder() when you're ready to order. Both calls return a receipt
# object that you can use for your records.
# Once your order is placed it'll go through SoftLayer's approval and
# provisioning process. When it's done you'll have a new
# SoftLayer_Hardware_Server object and server ready to use.
receipt = client['Product_Order'].verifyOrder(orderTemplate)
print(json.dumps(receipt, sort_keys=True, indent=2, separators=(',', ': ')))

```

```

[^1]:https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group
