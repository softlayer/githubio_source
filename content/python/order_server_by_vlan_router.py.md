---
title: "Order a Virtual and Bare Metal Server by frondend/backend vlan or router"
description: Examples to order a Virtual and Bare Metal Server by frondend/backend vlan or router"
date: "2020-11-26"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Account"
tags:
    - "order"
    - "vlan"
    - "pricing"
    - "create"
    - "filter"
    - "hardware"
    - "package"
    - "router"
---

### Order a Bare Metal by frondend/backend vlan or router.

Example of how to build an order for a bare metal server.

    1. Find the package that you want to order. listServerPackages() will filter out all that are not bare metal 
    servers.
    
    2. Use getServerPrices() to find the item keyNames you want to include in your order. These price IDs can be 
    included prices array directly, but I’ve included gatherPriceIds() to match up KeyNames to build a list of price 
    ids. getServerPrices() will also show the locations available for ordering.
    
    3. listAvailableVlans() if you want to place the server on a specific VLAN.
    
    4. listAvailableRouters() if you want to place the server on a specific router.

```python
from pprint import pprint as pp
import SoftLayer
from prettytable import PrettyTable


class Ordering:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()

    def main(self, package_id, location_id, frontend, backend, network_component_type):
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
        ]
        """We need bandwidth, at least 1 ip, and the port speed """
        network_items = [
            'BANDWIDTH_500_GB',
            '1_IP_ADDRESS',
            '100_MBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS',
        ]
        """A disk controller, a duplicate entry for each disk you want, in order, ram, OS and processor chip """
        physical_items = [
            'DISK_CONTROLLER_NONRAID',
            'HARD_DRIVE_1_00_TB_SATA_2',
            'RAM_64_GB_DDR4_2133_ECC_NON_REG',
            'OS_WINDOWS_2016_FULL_STD_64_BIT',
            'INTEL_INTEL_XEON_E52620_V4_2_10',
        ]

        if network_component_type == "vlan":
            primaryNetworkComponent = {
                "networkVlan": {
                    "id": frontend
                }
            }
            primaryBackendNetworkComponent = {
                "networkVlan": {
                    "id": backend
                }
            }
        else:
            primaryNetworkComponent = {
                "router": {
                    "id": frontend
                }
            }
            primaryBackendNetworkComponent = {
                "router": {
                    "id": backend
                }
            }

        all_items = required_items + network_items + physical_items
        prices = self.gatherPriceIds(package_id, all_items)
        product_order = {'orderContainers': [
            {
                'hardware':
                    [
                        {
                            'domain': u'cgallo.com',
                            'hostname': u'vmware-testing01',
                            "primaryNetworkComponent": primaryNetworkComponent,
                            "primaryBackendNetworkComponent": primaryBackendNetworkComponent
                        }
                    ],
                'location': location_id,
                'packageId': package_id,
                'prices': prices,
                'quantity': 1
            }
        ]
        }
        pp(product_order)
        order = self.client['Product_Order'].verifyOrder(product_order)
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

    def listAvailableVlans(self, dc_id, package_id):
        result = self.client['SoftLayer_Product_Order'].getVlans(dc_id, package_id)
        print(result)

        public_vlans = result['publicVlans']

        private_vlans = result['privateVlans']
        table_public_vlan = PrettyTable()
        table_public_vlan.title = "Available Public Vlans"
        table_public_vlan.field_names = ["id", "VlanNumber", "HostnameDatacenter", "HostnameRouter"]
        for public_vlan in public_vlans:
            table_public_vlan.add_row([public_vlan['id'],
                                       public_vlan['vlanNumber'],
                                       public_vlan['hostnameDatacenter'],
                                       public_vlan['hostnameRouter']
                                       ]
                                      )
        print(table_public_vlan)

        table_private_vlan = PrettyTable()
        table_private_vlan.title = "Available Private Vlans"
        table_private_vlan.field_names = ["id", "VlanNumber", "HostnameDatacenter", "HostnameRouter"]
        for private_vlan in private_vlans:
            table_private_vlan.add_row([private_vlan['id'],
                                        private_vlan['vlanNumber'],
                                        private_vlan['hostnameDatacenter'],
                                        private_vlan['hostnameRouter']
                                        ]
                                       )
        print(table_private_vlan)

    def listAvailableRouters(self, dc_id):
        _filter = {
            'routers': {
                'topLevelLocation': {'id': {'operation': dc_id}}
            }
        }
        result = self.client['SoftLayer_Account'].getRouters(filter=_filter)
        table = PrettyTable()
        table.title = "Available Routers"
        table.field_names = ["id", "hostname", "topLevelLocation"]
        for vlan in result:
            table.add_row([vlan['id'],
                           vlan['hostname'],
                           vlan['topLevelLocation']['longName'],
                           ]
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
                if not prices['locationGroupId']:
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
                if not prices['locationGroupId']:
                    table.add_row([prices['id'],
                                   str(item['description']).replace(" - ", "\n"),
                                   prices.get('recurringFee', '?'),
                                   item['keyName']])
        print(table)

    def gatherPriceIds(self, package_id, keyNames):
        # This wont work for prices that have core requirements
        mask = 'mask[id,itemCategory,keyName,prices[categories]]'
        items = self.client['Product_Package'].getItems(mask=mask, id=package_id)

        prices = []
        category_dict = {"gpu0": -1, "pcie_slot0": -1}

        for item_keyname in keyNames:
            try:
                matching_item = [i for i in items if i['keyName'] == item_keyname][0]
            except IndexError:
                raise SoftLayer.SoftLayerError(
                    "Item {} does not exist for package {}".format(item_keyname,
                                                                   package_id))

            item_category = matching_item['itemCategory']['categoryCode']

            if item_category not in category_dict:
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
    
    Remove the comment symbol '#' below to get the 'listServerPackages' information.
    """
    # main.listServerPackages()
    package_id = 553

    """
    Step 2, collect all the pieces you want to order
    getServerPrices will list out all the keyNames and cost of components
    that can be ordered on a certain package. Will also list the DCs that this
    server is available in.
    
    Remove the comment symbol '#' below to 'getServerPrices' information.
    """
    # main.getServerPrices(package_id)
    location_id = 1854895  # "DALLAS13"

    """
    Step 3, will list all available public and private vlans.

    Remove the comment symbol '#' below to 'listAvailableVlans' information.
    """
    # main.listAvailableVlans(location_id, package_id)
    pub_vlan_id = 1401234
    priv_vlan_id = 2282123

    """
    Step 4, will list all available routers.

    Remove the comment symbol '#' below to 'listAvailableRouters' information.
    """
    # main.listAvailableRouters(location_id)
    pub_router_id = 1074345
    priv_router_id = 1884234

    """
    Step 5, To order a bare metal server by backend/frontend vlan.
    
    Remove the comment symbol '#' below to order a bare metal server.
    """
    # main.main(package_id, location_id, pub_vlan_id, priv_vlan_id, "vlan")

    """
    Step 6, To order a bare metal server by backend/frontend router.
    
    Remove the comment symbol '#' below to order a bare metal server.
    """
    # main.main(package_id, location_id, pub_router_id, priv_router_id, "router")

```


### Order a Virtual Server by backend/frontend vlan or router

Example of how to build an order for a virtual server.

    1. Find the package that you want to order. listServerPackages() will filter out all VIRTUAL_SERVER_INSTANCE.
    
    2. Use getServerPrices() to find the item keyNames you want to include in your order. These price IDs can be 
    included prices array directly, but I’ve included gatherPriceIds() to match up KeyNames to build a list of price 
    ids. getServerPrices() will also show the locations available for ordering.
    
    3. listActivePresets() will list all active presets for a specific package.
    
    4. listAvailableVlans() if you want to place the server on a specific VLAN.
    
    5. listAvailableRouters() if you want to place the server on a specific router.

```python
from pprint import pprint as pp

import SoftLayer
from prettytable import PrettyTable


class Ordering:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()

    def main(self, package_id, location_id, frontend, backend, preset_id, network_component_type):
        """
        Places an order for a Virtual Server Instance
        """

        """These items are required for all servers and have a 0$ cost, some can be upgraded"""
        required_items = [
            'REBOOT_REMOTE_CONSOLE',
            'MONITORING_HOST_PING',
            'NOTIFICATION_EMAIL_AND_TICKET',
            'AUTOMATED_NOTIFICATION',
            'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT',
        ]
        """We need bandwidth, at least 1 ip, and the port speed """
        network_items = [
            'BANDWIDTH_0_GB_2',
            '1_IP_ADDRESS',
            '100_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS',
        ]

        physical_items = [
            'OS_WINDOWS_2012_R2_FULL_STD_64_BIT',
        ]

        primaryBackendNetworkComponent, primaryNetworkComponent = self.configureNetworkComponents(backend,
                                                                                                  frontend,
                                                                                                  network_component_type
                                                                                                  )

        all_items = required_items + network_items + physical_items
        prices = self.gatherPriceIds(package_id, preset_id, all_items)
        product_order = {'orderContainers': [
            {
                "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
                'virtualGuests':
                    [
                        {
                            'domain': u'test.com',
                            'hostname': u'vmware-testing01',
                            "primaryNetworkComponent": primaryNetworkComponent,
                            "primaryBackendNetworkComponent": primaryBackendNetworkComponent
                        }
                    ],
                "useHourlyPricing": True,
                'location': location_id,
                'packageId': package_id,
                'presetId': preset_id,
                'prices': [{'id': price_id} for price_id in prices],
                'quantity': 1
            }
        ]
        }
        pp(product_order)
        order = self.client['Product_Order'].verifyOrder(product_order)
        # order = self.client['Product_Order'].placeOrder(productOrder)
        pp(order)

    def configureNetworkComponents(self, backend, frontend, network_component_type):
        if network_component_type == "vlan":
            primaryNetworkComponent = {
                "networkVlan": {
                    "id": frontend
                }
            }
            primaryBackendNetworkComponent = {
                "networkVlan": {
                    "id": backend
                }
            }
        else:
            primaryNetworkComponent = {
                "router": {
                    "id": frontend
                }
            }
            primaryBackendNetworkComponent = {
                "router": {
                    "id": backend
                }
            }
        return primaryBackendNetworkComponent, primaryNetworkComponent

    def listServerPackages(self):
        mask = "mask[type]"
        _filter = {
            'type': {
                'keyName': {'operation': 'VIRTUAL_SERVER_INSTANCE'},
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

    def listAvailableVlans(self, dc_id, package_id):
        result = self.client['SoftLayer_Product_Order'].getVlans(dc_id, package_id)
        print(result)

        public_vlans = result['publicVlans']

        private_vlans = result['privateVlans']
        table_public_vlan = PrettyTable()
        table_public_vlan.title = "Available Public Vlans"
        table_public_vlan.field_names = ["id", "VlanNumber", "HostnameDatacenter", "HostnameRouter"]
        for public_vlan in public_vlans:
            table_public_vlan.add_row([public_vlan['id'],
                                       public_vlan['vlanNumber'],
                                       public_vlan['hostnameDatacenter'],
                                       public_vlan['hostnameRouter']
                                       ]
                                      )
        print(table_public_vlan)

        table_private_vlan = PrettyTable()
        table_private_vlan.title = "Available Private Vlans"
        table_private_vlan.field_names = ["id", "VlanNumber", "HostnameDatacenter", "HostnameRouter"]
        for private_vlan in private_vlans:
            table_private_vlan.add_row([private_vlan['id'],
                                        private_vlan['vlanNumber'],
                                        private_vlan['hostnameDatacenter'],
                                        private_vlan['hostnameRouter']
                                        ]
                                       )
        print(table_private_vlan)

    def listAvailableRouters(self, dc_id):
        _filter = {
            'routers': {
                'topLevelLocation': {'id': {'operation': dc_id}}
            }
        }
        result = self.client['SoftLayer_Account'].getRouters(filter=_filter)
        table = PrettyTable()
        table.title = "Available Routers"
        table.field_names = ["id", "hostname", "topLevelLocation"]
        for vlan in result:
            table.add_row([vlan['id'],
                           vlan['hostname'],
                           vlan['topLevelLocation']['longName'],
                           ]
                          )
        print(table)

    def listActivePresets(self, package_id):
        result = self.client["SoftLayer_Product_Package"].getActivePresets(id=package_id)
        table = PrettyTable()
        table.title = "Active Presets"
        table.field_names = ["id", "description", "keyName"]
        for preset in result:
            table.add_row([preset['id'],
                           preset['description'],
                           preset['keyName'],
                           ]
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
                if not prices['locationGroupId']:
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
                if not prices['locationGroupId']:
                    table.add_row([prices['id'],
                                   str(item['description']).replace(" - ", "\n"),
                                   prices.get('recurringFee', '?'),
                                   item['keyName']])
        print(table)

    def gatherPriceIds(self, package_id, preset_id, items):
        # This will work for prices that have core requirements
        mask = 'mask[prices[item]]'
        filter_preset = {
            'activePresets': {
                'id': {'operation': preset_id}
            }
        }
        preset_list = self.client["SoftLayer_Product_Package"].getActivePresets(mask=mask, filter=filter_preset,
                                                                                id=package_id)
        item_prices = self.client["SoftLayer_Product_Package"].getItemPrices(mask='mask[item]', id=package_id)
        capacity = 0
        for preset in preset_list:
            for price in preset['prices']:
                if "CORE" in price['item']['keyName']:
                    capacity = price['item']['capacity']

        prices = []
        for keyname_item in items:
            for item_price in item_prices:
                if keyname_item == item_price['item']['keyName']:
                    if 'capacityRestrictionMinimum' in item_price:
                        capacityMinimun = item_price['capacityRestrictionMinimum']
                        capacityMaximum = item_price['capacityRestrictionMaximum']
                        if capacityMinimun >= capacity and capacityMaximum <= capacity:
                            prices.append(item_price['id'])
                    else:
                        prices.append(item_price['id'])

        return prices


if __name__ == "__main__":
    main = Ordering()

    """
    Step 1, find the package server type you want    
    e.g. 835  PUBLIC_CLOUD_SERVER
    Remove the comment symbol '#' below to get the 'listServerPackages' information.
    """
    # main.listServerPackages()
    package_id = 835

    """
    Step 2, collect all the pieces you want to order
    getServerPrices will list out all the keyNames and cost of components
    that can be ordered on a certain package. Will also list the DCs that this
    server is available in.

    Remove the comment symbol '#' below to 'getServerPrices' information.
    """
    # main.getServerPrices(package_id)
    location_id = 1441195  # "DALLAS10"

    """
    Step 3, will list all active presets.

    Remove the comment symbol '#' below to 'getServerPrices' information.
    """
    # main.listActivePresets(package_id)
    preset_id = 345  # "B1_8X16X100"

    """
    Step 4, will list all available public and private vlans.

    Remove the comment symbol '#' below to 'listAvailableVlans' information.
    """
    # main.listAvailableVlans(location_id, package_id)
    pub_vlan_id = 1401234
    priv_vlan_id = 221234

    """
    Step 5, will list all available routers.

    Remove the comment symbol '#' below to 'listAvailableRouters' information.
    """
    # main.listAvailableRouters(location_id)
    pub_router_id = 1071234
    priv_router_id = 1881234

    """
    Step 6, To order a virtual server by backend/frontend vlan.

    Remove the comment symbol '#' below to order a virtual server.
    """

    # main.main(package_id, location_id, pub_vlan_id, priv_vlan_id, preset_id, "vlan")

    """
    Step 7, To order a virtual server by backend/frontend router.

    Remove the comment symbol '#' below to order a virtual server.
    """

    # main.main(package_id, location_id, pub_router_id, priv_router_id, preset_id, "router")


```