---
title: "os_reload_configuration_page.py"
description: "os_reload_configuration_page.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Software_Component"
    - "SoftLayer_SoftLayer_Product_Package"
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Item_Resource_Conflict"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Display the information about the server to reload like the Softlayer portal.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_SoftLayer_Product_Package
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem
http://sldn.softlayer.com/reference/services/SoftLayer_SoftLayer_Product_Package/getItemConflicts

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer


def get_hardware(hardware_id, hardware_service):
    """Get the hardware object.
        :param int hardware_id: The id of the hardware to get.
        :param SoftLayer_Hardware_Server hardware_service: The SoftLayer_Hardware_Server service.
        :returns: A Softlayer_Hardware_Server object.
    """
    object_mask = 'mask[account[attributes[accountAttributeType]], activeTransaction[transactionStatus], ' \
                  'billingItem[item[totalPhysicalCoreCapacity, capacity], ' \
                  'package[configuration[itemCategory[categoryCode, name]], ' \
                  'items[availabilityAttributes[attributeTypeKeyName], coreRestrictedItemFlag, ' \
                  'prices[accountRestrictions, categories[categoryCode, name], requiredCoreCount, ' \
                  'definedSoftwareLicenseFlag], requirements, softwareDescription[averageInstallationDuration]]]],' \
                  'hourlyBillingFlag, managedResourceFlag, operatingSystem[averageInstallationDuration, ' \
                  'passwords[sshKeys]], primaryIpAddress, ' \
                  'softwareComponents[softwareLicense[softwareDescription[features[keyName],' \
                  'productItems[categories[categoryCode, name]]]]], networkGatewayMemberFlag]'
    try:
        hardware = hardware_service.getObject(id=hardware_id, mask=object_mask)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the hardware: \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))
        exit(1)
    return hardware


def get_item_conflicts(hardware, package_service):
    """Get all the items conflict of the package which belongs the hardware.
        :param SoftLayer_Hardware_Server hardware: The server to get its item conflicts.
        :param SoftLayer_Product_Package package_service: The SoftLayer_Product_Package service.
        :returns: an array of SoftLayer_Product_Item_Resource_Conflict.
    """
    return package_service.getItemConflicts(id=hardware['billingItem']['package']['id'])


def is_active_transaction(hardware):
    """Get whether there is an active transaction running for the server.
        :param SoftLayer_Hardware_Server hardware: The server to get its item conflicts.
        :returns: a boolean value.
    """
    if 'activeTransaction' in hardware:
        return True
    else:
        return False


def get_software(hardware, category_code):
    """Get intalled software in a server.
        :param SoftLayer_Hardware_Server hardware: The server to get its item conflicts.
        :param string category_code: The category code of the software to ger.
        :returns: a SoftLayer_Software_Component object.
    """
    software = hardware['softwareComponents']
    filtered_software = {}
    for item in software:
        for productItem in item['softwareLicense']['softwareDescription']['productItems']:
            for category in productItem['categories']:
                if category['categoryCode'] == category_code:
                    filtered_software = item
                    break
    return filtered_software


def get_current_software(hardware):
    """Get all the installed software in a server.
        :param SoftLayer_Hardware_Server hardware: The server to get its item conflicts.
        :returns: a array of SoftLayer_Software_Component.
    """
    software = {}
    items = []
    software['os'] = get_software(hardware, 'os')
    software['os_addon'] = get_software(hardware, 'os_addon')
    software['control_panel'] = get_software(hardware, 'control_panel')
    software['database'] = get_software(hardware, 'database')
    software['av_spyware_protection'] = get_software(hardware, 'av_spyware_protection')
    software['firewall'] = get_software(hardware, 'firewall')
    if 'softwareLicense' in software['os']:
        items = items + software['os']['softwareLicense']['softwareDescription']['productItems']
    if 'softwareLicense' in software['os_addon']:
        items = items + software['os_addon']['softwareLicense']['softwareDescription']['productItems']
    if 'softwareLicense' in software['control_panel']:
        items = items + software['control_panel']['softwareLicense']['softwareDescription']['productItems']
    if 'softwareLicense' in software['database']:
        items = items + software['database']['softwareLicense']['softwareDescription']['productItems']
    if 'softwareLicense' in software['av_spyware_protection']:
        items = items + software['av_spyware_protection']['softwareLicense']['softwareDescription']['productItems']
    if 'softwareLicense' in software['firewall']:
        items = items + software['firewall']['softwareLicense']['softwareDescription']['productItems']
    software['items'] = items
    return software


def get_item_prices(hardware, category_code, current_software, item_conflicts):
    """ Get all available prices for a category code filtering the item conflicts.
        :param SoftLayer_Hardware_Server hardware: The server to get its item conflicts.
        :param string category_code: the category code to get the prices.
        :param An array of SoftLayer_Software_Component current_software: The installed software in the server.
        :param An array of SoftLayer_Product_Item_Resource_Conflict item_conflicts:
        The item conflicts in the package of the server.
        :returns: a array of SoftLayer_Software_Component.
    """
    items = hardware['billingItem']['package']['items']
    filter_items = []
    for item in items:
        if 'prices' in item:
            for price in item['prices']:
                item_added = False
                for category in price['categories']:
                    if category['categoryCode'] == category_code:
                        has_conflict = False
                        for conflict in item_conflicts:
                            if conflict['itemId'] == item['id']:
                                for software_item in current_software['items']:
                                    if software_item['id'] == conflict['resourceTableId']:
                                        has_conflict = True
                                        break
                            if has_conflict:
                                break
                        if not has_conflict:
                            filter_items.append(item)
                            item_added = True
                            break
                if item_added:
                    break
    return filter_items


def display(items, current_software):
    """Displays all the items for the reload.
        :param SoftLayer_Product_Item items: The items to display.
        :param An array of SoftLayer_Software_Component current_software: The installed software in the server.
    """
    if 'softwareLicense' in current_software:
        print(" Current: " + current_software['softwareLicense']['softwareDescription']['productItems'][0]
                                             ['categories'][0]['name'] +
              ': ' + current_software['softwareLicense']['softwareDescription']['productItems'][0]['description'])
    else:
        print(" Current: None")
    print("    Items to select:")
    for i in items:
        print(" " * 10 + i['description'])
        for price in i['prices']:
            if price['locationGroupId'] == "":
                if 'hourlyRecurringFee' in price:
                    print(" " * 14 + "Price id: " + str(price['id']) + " Monthly: " + str(price['recurringFee'])
                          + " Hourly:" + str(price['hourlyRecurringFee']))
                else:
                    print(" " * 14 + "id: " + str(price['id']) + " Monthly: " + str(price['recurringFee']))
    return

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The hardware server id
hardware_id = 249266

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardware_service = client['SoftLayer_Hardware_Server']
package_service = client['SoftLayer_Product_Package']

hardware = get_hardware(hardware_id, hardware_service)

if is_active_transaction(hardware):
    print("There is a currently a transaction in progress for this device.")
    exit(1)

current_software = get_current_software(hardware)
item_conflicts = get_item_conflicts(hardware, package_service)

availableOs = get_item_prices(hardware, 'os', current_software, item_conflicts)
availableOsAddom = get_item_prices(hardware, 'os_addon', current_software, item_conflicts)
availableControlPanel = get_item_prices(hardware, 'control_panel', current_software, item_conflicts)
availableDatabase = get_item_prices(hardware, 'database', current_software, item_conflicts)
availableAntivir = get_item_prices(hardware, 'av_spyware_protection', current_software, item_conflicts)
availableFirewall = get_item_prices(hardware, 'firewall', current_software, item_conflicts)

display(availableOs, current_software['os'])
display(availableOsAddom, current_software['os_addon'])
display(availableControlPanel, current_software['control_panel'])
display(availableDatabase, current_software['database'])
display(availableAntivir, current_software['av_spyware_protection'])
display(availableFirewall, current_software['firewall'])

```
