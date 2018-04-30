---
title: "get_device_configuration_upgrade.py"
description: "get_device_configuration_upgrade.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Provisioning_Maintenance_Window"
tags:
    - "baremetalservers"
---


```
"""
Display the hardware configuration and the items which can be modified in the server
like in the portal when the modify device configuration link is clicked in the
bare metal details page.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getUpgradeItemPrices/getMaintenanceWindows
http://sldn.softlayer.com/reference/services/SoftLayer_Provisioning_Maintenance_Window
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer.API
import datetime

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

server_ip = "159.8.52.185"

day_maintenance = "2017-10-10"

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardware_service = client['SoftLayer_Hardware_Server']
maintenance_service = client['SoftLayer_Provisioning_Maintenance_Window']


def get_maintenance(server, day_maintenance, maintenance_service):
    """Get the prices of the items to upgrade in a server.
         :param SoftLayer_Hardware_Server server: The server to get the maintenance date.
         :param string day_maintenance: The date to get the list of maintenance available.
         :param string maintenance_service: Declaring api cilent`s service.
         :returns: A array of SoftLayer_Provisioning_Maintenance_Window object.
    """
    end_date = datetime.datetime.strptime(day_maintenance, '%Y-%m-%d')
    start_date = end_date + datetime.timedelta(days=-1)
    result = maintenance_service.getMaintenanceWindows(str(start_date), str(end_date), server['datacenter']['id'])
    items = [item for item in result if day_maintenance in item['beginDate']]
    return items


def get_server(server_ip, hardware_service):
    """Get the server.
         :param string server_ip: The Ip address of the server.
         :param SoftLayer_Hardware_Server hardware_service: the SoftLayer_Hardware_Server service.
         :returns: A SoftLayer_Hardware_Server object.
    """
    try:
        object_mask = "mask[datacenter, activeTransaction[transactionStatus], billingItem[children[category, " \
                     "item], orderItem[order[items]], package[configuration[itemCategory[categoryCode, name]]]]," \
                     " hourlyBillingFlag, managedResourceFlag, primaryIpAddress, networkGatewayMemberFlag]"
        server = hardware_service.findByIpAddress(server_ip, mask=object_mask)
        if not server:
            print("There is no a server with the IP address: " + server_ip)
            exit(1)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to retrieve the server: \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))
        exit(1)
    return server


def get_upgrade_items(server, hardware_service):
    """Get the prices of the items to upgrade in a server.
         :param SoftLayer_Hardware_Server server: The server to get the upgrade item prices.
         :param SoftLayer_Hardware_Server hardware_service: the SoftLayer_Hardware_Server service.
         :returns: A array of SoftLayer_Product_Item_Price object.
    """
    try:
        upgrade_items = hardware_service.getUpgradeItemPrices(id=server['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to retrieve the upgrade items: \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))
        exit(1)
    return upgrade_items


def get_upgrade_items_by_categories(server, upgrade_items):
    """Get the prices of the items to upgrade in a server.
         :param SoftLayer_Hardware_Server server: The server to get the upgrade item prices.
         :param array of SoftLayer_Product_Item_Price upgrade_items: the item prices to upgrade.
         :returns: A array of item prices sorted by category.
    """
    categories = server['billingItem']['package']['configuration']
    items_by_category = []
    for cat in categories:
        upgrade_category = {'category': cat['itemCategory']}
        prices = []
        for item in upgrade_items:
            for cat_item in item['categories']:
                if cat_item['categoryCode'] == upgrade_category['category']['categoryCode']:
                    prices.append(item)
                    break
        upgrade_category['prices'] = prices
        if len(prices) > 0:
            current_conf = {}
            for conf in server['billingItem']['children']:
                if conf['categoryCode'] == upgrade_category['category']['categoryCode']:
                    current_conf = conf
                    break
            upgrade_category['currentInInstalled'] = current_conf
            items_by_category.append(upgrade_category)
    return items_by_category


def display_data(server, upgrade_categories, maintenances):
    """Get the prices of the items to upgrade in a server.
         :param SoftLayer_Hardware_Server server: The server to get the upgrade item prices.
         :param A array of upgrade_categories: The upgrade item prices.
         :param A array of SoftLayer_Provisioning_Maintenance_Window  maintenances: The maintanance date.
    """
    print("Maintenance")
    for item in maintenances:
        print(" " * 4 + "id: " + str(item['id']) + " Date: " + item['beginDate'] + " to " + item['end_date'])
    for item in upgrade_categories:
        print(item['category']['name'])
        if 'description' in item['currentInInstalled']:
            current = item['currentInInstalled']['item']['description']
            current_price = {}
            for price in item['prices']:
                if price['item']['description'] == current:
                    current_price = price
                    break
            if not 'recurringFee' in current_price:
                for price in item['prices']:
                    if price['categories'][0]['name'] == item['category']['name']:
                        current_price = price
                        current = price['item']['description']
            if not server['hourlyBillingFlag']:
                print(" " * 4 + "Current installed: " + current + " Price: " +
                      current_price['recurringFee'] + " per month")
            else:
                print(" " * 4 + "Current installed: " + current + " Price: " +
                      current_price['hourlyRecurringFee'] + "per hour")
        else:
            current = 'None'
            print(" " * 4 + "Current installed: " + current)
        print(" " * 4 + "Available items:")
        for price in item['prices']:
            if price['item']['description'] != current:
                if not server['hourlyBillingFlag']:
                    print(" " * 8 + price['item']['description'] + " Price: " +
                          price['recurringFee'] + " per month")
                else:
                    print(" " * 8 + price['item']['description'] + " Price: " +
                          price['hourlyRecurringFee'] + " per hour")
    return

server = get_server(server_ip, hardware_service)
upgrade_items = get_upgrade_items(server, hardware_service)
upgrade_categories = get_upgrade_items_by_categories(server, upgrade_items)
maintenances = get_maintenance(server, day_maintenance, maintenance_service)
display_data(server, upgrade_categories, maintenances)

```
