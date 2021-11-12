---
title: "List items for a Server Order"
description: "The script displays the available data centers and items for a package."
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item"
    - "SoftLayer_Location_Datacenter"
    - "SoftLayer_Product_Package_Preset_Configuration"
    - "SoftLayer_Product_Package_Order_Configuration"
    - "SoftLayer_Product_Package_Preset"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Location_Region"
tags:
    - "server"
    - "ordering"
---

This is an older article, the following might provide better instructions.
- [The Catalog](/article/catalog/)
- [SLCLI Ordering](/article/understanding-ordering/)
- [Basic and Advanced Ordering](/article/understanding-ordering-basics/)

```python
"""
List items to order device.

The script displays the available data centers and items for a package.
Note: The displayed prices are standard prices.
"""

import SoftLayer


package_id = 200
# Set True to see the hourly prices.
# In case you see empty prices that means the item does not have an hourly price.
hourly = False

# Some packages such as the package 200 requires a preset id.
# Configure the value with "" in case the packages do not requires a preset id.
preset_id = 385

client = SoftLayer.create_client_from_env()
package_service = client['SoftLayer_Product_Package']


def get_all_datacenters_available_for_package(package_id, package_service):
    """Get the available datacenters for a package.
        :param int package_id: The package id to get the available data centers.
        :param SoftLayer_Product_Package package_service: The SoftLayer Product Package service.
        :returns: An array SoftLayer_Location_Region.
    """
    try:
        object_mask = "mask[regions[keyname,description,sortOrder," \
                      "location[location(SoftLayer_Location_Datacenter)[activePresaleEvents," \
                      "priceGroups.id,locationAddress.country,brandCountryRestrictions[locationId, " \
                      "customerCountryCode]]]]]"
        result = package_service.getObject(id=package_id, mask=object_mask)
        regions = []
        for item in result['regions']:
            for detail in item['location']['locationPackageDetails']:
                if detail['isAvailable'] == 1 and detail['locationId'] == item['location']['location']['id'] \
                        and detail['packageId'] == package_id:
                    regions.append(item)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the data centers. \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))
        exit(0)
    return regions


def get_all_items(package_id, package_service):
    """Get all the items for a package.
        :param int package_id: The package id to get the available data centers.
        :param SoftLayer_Product_Package package_service: The SoftLayer Product Package service.
        :returns: An array of SoftLayer_Product_Item.
    """
    try:
        object_mask = "mask[categories, prices[pricingLocationGroup, presetConfigurations]]"
        items = package_service.getItems(id=package_id, mask=object_mask)
        items = sorted(items, key=lambda item: (item['description']))
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the items. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
        exit(0)
    return items


def get_configuration(package_service):
    """Get the configuration for a package.
        :param SoftLayer_Product_Package package_service: The SoftLayer Product Package service.
        :returns: An array of SoftLayer_Product_Package_Order_Configuration.
    """
    try:
        object_mask = "mask[itemCategory]"
        items = package_service.getConfiguration(id=package_id, mask=object_mask)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the required categories. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
        exit(0)
    return items


def is_required_option(list, category_code, configurations):
    """Verifies if a category is required in the configurations of the package
       In case it is not required adds the value none to the list parameter.
        :param An array of SoftLayer_Product_Item list: The list of items.
        :param string category_code: The category code to verify if it is required in the package configuration.
        :param An array of SoftLayer_Product_Package_Order_Configuration configurations:
        The configuration of the package.
        :returns: An array of SoftLayer_Product_Item.
    """
    items = [conf for conf in configurations if conf['itemCategory']['categoryCode'] == category_code
             and conf['isRequired'] == 1]
    if len(items) == 0:
        none = {}
        none['description'] = "None"
        list.insert(0, none)
    return list


def get_filtered_items_category(items, configurations, category_code):
    """Gets the items which belong to a category code.
        :param An array of SoftLayer_Product_Item items: The list of items.
        :param An array of SoftLayer_Product_Package_Order_Configuration configurations:
        The configuration of the package.
        :param string category_code: The category code to filter.
        :returns: An array of SoftLayer_Product_Item.
    """
    filtered = []
    for item in items:
        categories = [category for category in item['categories'] if category['categoryCode'] == category_code]
        if len(categories) > 0:
            filtered.append(item)
    filtered = is_required_option(filtered, category_code, configurations)
    return filtered


def get_standard_item_price(item):
    """Gets the standard price for an item.
        :param An array of SoftLayer_Product_Item item: The item to get the standard price.
        :returns: A SoftLayer_Product_Item_Price.
    """
    prices = [price for price in item['prices'] if price['locationGroupId'] == ""]
    # We always return the last standard price in the list.
    return prices[-1]


def display_datacenters(datacenters):
    """Displays the data centers.
        :param An array SoftLayer_Location_Region datacenters: The list of regions.
    """
    tab_spaces_begin = 4
    id_label = "LocationId"
    print(id_label + " " * tab_spaces_begin + "DATA CENTER")
    for datacenter in datacenters:
        print(str(datacenter['location']['location']['id']) + " " *
              (len(id_label) - len(str(datacenter['location']['location']['id']))) + " " *
              tab_spaces_begin + datacenter['description'])
    print()
    print()
    return


def display_items(items, title, hourly, is_preset, price_preset):
    """Displays the data centers.
        :param An array SoftLayer_Product_Item items: The list of items to display.
        :param string title: The title of the items.
        :param boolean hourly: A boolean value which indicates if the hourly prices must be displayed.
    """
    tab_spaces_begin = 4
    tab_spaces_prices = 4
    tab_spaces_desc = 60
    price_id_label = "PriceId"
    if len(items) > 0:
        if len(items) > 1 or items[0]['description'] != "None":
            if not hourly:
                price_label = "Monthly"
                price_key = "recurringFee"
            else:
                price_label = "Hourly"
                price_key = "hourlyRecurringFee"

            print(price_id_label + " " * tab_spaces_begin + title.upper() + " " * tab_spaces_desc + price_label +
                  " " * tab_spaces_prices + "Setup")
            for item in items:
                if item['description'] == "None":
                    print(" " * len(price_id_label) + " " * tab_spaces_begin + item['description'])
                else:
                    if not is_preset:
                        price = get_standard_item_price(item)
                    else:
                        price = price_preset
                    if price_key in price:
                        print(str(price['id']) + " " * (len(price_id_label) - len(str(price['id']))) + " "
                              * tab_spaces_begin + item['description'].strip() + " "
                              * (tab_spaces_desc + len(title) - len(item['description']))
                              + str(float(price[price_key])) + "$" + " "
                              * (len(price_label) - len(str(float(price[price_key]))))
                              + " " * tab_spaces_prices + str(float(price['setupFee'])) + "$")
            print()
            print()
    return


def is_preset_required(package_id, package_service):
    """Gets the preset configuration required flag.
        :param int package_id: The package id to get the available data centers.
        :param SoftLayer_Product_Package package_service:
        The SoftLayer Product Package service.
        :returns: An boolean which indicates whether preset is required.
    """
    try:
        result = package_service.getPresetConfigurationRequiredFlag(id=package_id)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the preset configuration required flag. \nfaultCode= %s, \nfaultString= %s"
              % (e.faultCode, e.faultString))
        exit(0)
    return result


def getting_package_preset(package_id, preset_id, package_service):
    """Gets a SoftLayer_Product_Package_Preset object.
        :param int package_id: The package id to get the available data centers.
        :param int preset_id: The preset id of the SoftLayer_Product_Package_Preset to get.
        :param SoftLayer_Product_Package package_service: The SoftLayer Product Package service.
        :returns: A oftLayer_Product_Package_Preset object.
    """
    try:
        object_mask = "mask[packageConfiguration[itemCategory],categories, " \
                      "configuration[price[item[prices[pricingLocationGroup]]],category]]"
        object_filter = {"activePresets": {"id": {"operation": preset_id}}}
        presets = package_service.getActivePresets(id=package_id, mask=object_mask, filter=object_filter)
        if len(presets) == 0:
            print("The configured preset id: '" + str(preset_id) + "' is not valid for the package id: '"
                  + str(package_id) + "'")
            exit(0)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the active presets. \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))
        exit(0)
    return presets[0]


def get_filtered_item_preset_category(preset_configurations, category_code):
    """Gets the prices for a preset configuration list which contain an arbitrary category code.
        :param SoftLayer_Product_Package_Preset_Configuration preset_configurations:
        The list of configuration in the preset.
        :param string category_code: The category code to filter.
        :returns: An array SoftLayer_Product_Item_Price.
    """
    filtered = []
    for presetConfiguration in preset_configurations:
        if presetConfiguration['category']['categoryCode'] == category_code:
            filtered.append(presetConfiguration['price'])
    return filtered


def get_configurations_not_preset(preset):
    """Gets the configuration list which contains the categories that can be configurable.
        :param SoftLayer_Product_Package_Preset preset: The preset to get the configuration list.
        :returns: An array of SoftLayer_Product_Package_Order_Configuration.
    """
    configurations = []
    # When the package has a preset configuration only a few categories can be edited.
    # Below the list of categories which can be edited.
    allowed_list = ["bandwidth", "port_speed", "sec_ip_addresses", "pri_ipv6_addresses",
                    "static_ipv6_addresses", "evault", "os"]
    for conf in preset['packageConfiguration']:
        for allowed in allowed_list:
            if conf['itemCategory']['categoryCode'] == allowed:
                configurations.append(conf)
                break
    return configurations

# Getting the available data centers.
datacenters = get_all_datacenters_available_for_package(package_id, package_service)
# Displaying the data centers
display_datacenters(datacenters)

if not is_preset_required(package_id, package_service):
    # Getting the items in the package
    items = get_all_items(package_id, package_service)
    # Getting the configuration of the package
    configurations = get_configuration(package_id, package_service)
    configurations = sorted(configurations, key=lambda item: item['isRequired'], reverse=True)
    # Displaying the items
    for conf in configurations:
        listItems = get_filtered_items_category(items, configurations, conf['itemCategory']['categoryCode'])
        display_items(listItems, conf['itemCategory']['name'], hourly, False, "")
else:
    # Getting the preset configuration, these items cannot be changed in the order.
    # Review http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Preset for more information.
    preset = getting_package_preset(package_id, preset_id, package_service)
    print("*************************************   PRESET CONFIGURATION   *************************************")
    print("")
    for conf in preset['packageConfiguration']:
        listConfiguredItems = get_filtered_item_preset_category(preset['configuration'],
                                                                conf['itemCategory']['categoryCode'])
        items = []
        if len(listConfiguredItems) > 0:
            items.append(listConfiguredItems[0]['item'])
            display_items(items, conf['itemCategory']['categoryCode'], hourly, True, listConfiguredItems[0])
    # Getting the items which can be configured in the order.
    configurations = get_configurations_not_preset(preset)
    # Getting the items in the package
    items = get_all_items(package_id, package_service)
    print("*************************************   CONFIGURABLE ITEMS   *************************************")
    print("")
    # Displaying the items
    for conf in configurations:
        listItems = get_filtered_items_category(items, configurations, conf['itemCategory']['categoryCode'])
        display_items(listItems, conf['itemCategory']['name'], hourly, False, "")

```
