---
title: "Advanced Bare Metal Server Ordering"
description: "Explains how to build a bare metal order, includes how to get packages, prices, raid setup and vlans"
date: "2017-09-13"
classes:
    - "SoftLayer_Product_Order"
    - "SoftLayer_Configuration_Storage_Group_Array_Type"
    - "SoftLayer_Product_Package"
tags:
    - "order"
    - "vlan"
    - "bare-metal"
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



class ordering():

    def __init__(self):

        self.client = SoftLayer.Client()

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
            'NESSUS_VULNERABILITY_ASSESSMENT_REPORTING',
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
            'RAM_128_GB_DDR3_1333_REG_2',
            'OS_VSPHERE_ENTERPRISE_PLUS_6_0',
            'INTEL_XEON_2620_2_00'
        ]

        all_items = required_items + network_items + physical_items
        prices = self.gatherPriceIds(package_id, all_items)
        productOrder = {'orderContainers': [
                {'hardware': 
                    [
                        {
                            'domain': u'cgallo.com',
                            'hostname': u'vmware-testing01',
                            'primaryBackendNetworkComponent': {'networkVlanId': priv_vlan_id},
                            'primaryNetworkComponent': {'networkVlanId': pub_vlan_id}
                        }
                    ],
                    'location': location_id,
                    'packageId': package_id,
                    'prices': prices,
                    'quantity': 1,
                    'storageGroups' : [
                        {
                            'arrayTypeId': 2,
                            'hardDrives': [0,1],
                            'partitionTemplateId' : 1
                        },
                        {
                            'arrayTypeId': 9,
                            'arraySize' : 2000,
                            'hardDrives': [2],
                            'partitions' : [
                                {'name' : '/', 'size': 200, 'isGrow': 0},
                                {'name' : '/boot', 'size': 100},
                                {'name' : '/usr', 'size': 200},
                                {'name' : '/mine', 'size': 200},
                                {'name' : '/media', 'size': 1, 'isGrow': 1},
                            ]

                        },
                        {
                            'arrayTypeId': 9,
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

        for product in result:
            print("%s - %s - %s - %s" % 
                (product['id'],
                 product['name'],
                 product['keyName'],
                 product['type']['keyName'])
            )
            

    def listPartitionTemplates(self):
        mask = "mask[partitionTemplates[data]]"
        result = self.client['SoftLayer_Hardware_Component_Partition_OperatingSystem'].getAllObjects(mask=mask)
        print("OS Type, Notes")
        for os_type in result:
            print("%s - %s" % (os_type['description'],os_type['notes']))
            print("\tTemplate id, Description")
            for template in os_type['partitionTemplates']:
                print("\t%s - %s " % (template['id'],template['description']))
                for partition in template['data']:
                    print("\t\t%s - %s %s" % 
                        (partition['partitionName'], 
                         partition['partitionSize'], 
                         'Grow' if partition['isGrow'] else '')
                    )

    def listRaidArrayTypes(self):
        result = self.client['SoftLayer_Configuration_Storage_Group_Array_Type'].getAllObjects()
        for raid in result:
            print("%s - %s - %s Min:%s Max:%s" % 
                (raid['id'], 
                 raid['keyName'], 
                 raid['description'], 
                 raid['minimumDrives'], 
                 raid['maximumDrives'])
            ) 

    def listAvailableVlans(self, dc_id):
        mask = "mask[network,type,primaryRouter[datacenter]]"
        _filter = {
            'networkVlans' : {
                'primaryRouter': {
                    'datacenter' : { 'id': {'operation': dc_id} }
                }
            }
        }
        result = self.client['SoftLayer_Account'].getNetworkVlans(mask=mask,filter=_filter)
        for vlan in result:
            print("%s - VLAN: %s - Type: %s - %s " % 
                (vlan['id'], 
                 vlan['vlanNumber'],
                 vlan['type']['keyName'], 
                 vlan['primaryRouter']['hostname'])
            )

    def getServerPrices(self, package_id):
        mask = "mask[regions,items[prices],activeServerItems[prices]]"
        # locations = self.client['Product_Package'].getLocations(id=package_id)
        result = self.client['Product_Package'].getObject(mask=mask,id=package_id)
        print("Location ID, Location Name")
        for location in result['regions']:
            print("%s - %s " % (location['location']['location']['id'],location['description']))
        print("Price ID, description, Monthly Fee, KeyName")
        for item in result['items']:
            for prices in item['prices']:
                # only print the Default location price. 
                # The ordering system will replace the default price id for you if ordering in a non-usa region.
                if prices['locationGroupId'] is '':
                    # Some software has core restrictions that effect prices
                    if 'capacityRestrictionType' in prices:
                        cores = "%s - %s" % (
                             prices['capacityRestrictionMinimum'], 
                             prices['capacityRestrictionMaximum'])
                        print("%s, %s - %s cores, $%s, %s " % 
                            (prices['id'],
                             item['description'],
                             cores,prices.get('recurringFee','?'),
                             item['keyName'])
                        )
                    else:
                        print("%s, %s, $%s, %s " % 
                            (prices['id'],
                              item['description'],
                              prices.get('recurringFee','?'),
                              item['keyName'])
                        )
        print("======= SERVER ITEMS =======")
        # serverItems = self.client['Product_Package'].getActiveServerItems(id=package_id)
        print("Price ID, description, Monthly Fee, KeyName")
        for item in result['activeServerItems']:
            for prices in item['prices']:
                # only print the Default location price. 
                # The ordering system will replace the default price id for you if ordering in a non-usa region.
                if prices['locationGroupId'] is '':
                    print("%s, %s, $%s, %s " % 
                        (prices['id'],
                         item['description'],
                         prices.get('recurringFee','?'),
                         item['keyName'])
                    )


    def gatherPriceIds(self,package_id,keyNames):
        # This wont work for prices that have core requirements
        mask = "mask[items[prices],activeServerItems[prices]]"
        items = self.client['Product_Package'].getObject(mask=mask,id=package_id)

        prices = []
        sorted_items = {}

        for item in items['items']:
            for price in item['prices']:
                if price['locationGroupId'] is '': 
                    sorted_items[item['keyName']] = price['id']
        for item in items['activeServerItems']:
            for price in item['prices']:
                if price['locationGroupId'] is '': 
                    sorted_items[item['keyName']] = price['id']

        for keyName in keyNames:
            prices.append({'id': int(sorted_items.get(keyName))})
        return prices

if __name__ == "__main__":

    main = ordering()

    """
    Step 1, find the processor type you want
    269 - Quad E7-4800  Series (6 Drives) - 2U_QUAD_E74800_6_DRIVES : BARE_METAL_CPU
    """
    main.listServerPackages()
    package_id = 263

    """
    Step 2, collect all the pieces you want to order
    getServerPrices will list out all the keyNames and cost of components
    that can be ordered on a certain package. Will also list the DCs that this
    server is available in.
    """
    main.getServerPrices(package_id)
    location_id = 142776

    """
    Step 3, customize and place the order
    """
    main.listAvailableVlans(location_id)
    pub_vlan_id  = 2137279
    priv_vlan_id = 2137281
    main.listPartitionTemplates()
    main.listRaidArrayTypes()
    main.main(package_id,location_id,pub_vlan_id,priv_vlan_id)

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



[^1]:https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group
