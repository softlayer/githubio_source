---
title: "reload_os_server.py"
description: "reload_os_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Component_HardDrive"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Reload servers from a list of IPs

This script looks for a server with a determinate IP address and reload it

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json


def get_price(server, item_name):
    """Get the price for an item.
        :param SoftLayer_Hardware_Server server: The server to reload.
        :param string item_name: The item name to get the price.
        :returns: A Softlayer_Product_Item_Price object.
    """
    items = server['billingItem']['package']['items']
    prices = []
    for item in items:
        if 'description' in item:
            if item['description'].upper().strip() == item_name.upper().strip():
                prices = item['prices']
                break
    price = [price for price in prices if price['locationGroupId'] == '']
    if len(price) > 0:
        price = price[0]
    else:
        price = ''
    return price

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

ipsToReload = ['159.8.52.190', '10.104.213.250']

# The configuration for the reload.
# The values with empty value will not included in the reload request.
newOSToLoad = 'CentOS 6.x (64 bit)'
newOsAddom = 'XenServer Enterprise for XenServer 5.6'
newControlPanel = 'cPanel/WHM with Softaculous and RVskin'
newDatabase = ''
newAntivir = ''
newFirewall = ''
customProvisionScriptUri = ''
resetIpmiPassword = False
upgradeBios = False
upgradeHardDriveFirmware = False

# Partitions for the reload. If you do not want specify partions set the value empty hardDrives = []
# Each partition must have at least its name and minimumSize defined.
# Name defines your partition's mount point, and minimumSize specifies its size
# in gigabytes.
# UNIX partition schemes must have at least one swap partition, defined by the
# partition name /swap0. Set the partition's grow property to 1 to indicate that
# partition should expand to fill the remainder of the disk. You must have one
# grow partition in your partition scheme.
# Windows partitioning is a little simpler. Specify the C: partition with the
# name /os, with drives letters D:, E:, F:, etc as /disk0, /disk1, /disk2, and
# so on.
# This example sets up the following partition scheme:
#  * swap: 1G
#  * /boot: 100M
#  * /test: 15G
#  * /:  grown to fill disk space
hardDrives = [
    {
        'complexType': 'SoftLayer_Hardware_Component_HardDrive',
        'partitions': [
            {
                'name': '/swap0',
                'minimumSize': '1',
            },
            {
                'name': '/boot',
                'minimumSize': '.1',
            },
            {
                'name': '/test',
                'minimumSize': '15',
            },
            {
                'name': '/',
                'minimumSize': '1',
                'grow': '1',
            },
        ]
    }
]

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareService = client['SoftLayer_Hardware_Server']

objectMask = "mask[account[attributes[accountAttributeType]], activeTransaction[transactionStatus], " \
             "billingItem[item[totalPhysicalCoreCapacity, capacity], " \
             "package[configuration[itemCategory[categoryCode, name]], " \
             "items[availabilityAttributes[attributeTypeKeyName], coreRestrictedItemFlag, prices[accountRestrictions," \
             "categories[categoryCode, name], requiredCoreCount, definedSoftwareLicenseFlag], requirements, " \
             "softwareDescription[averageInstallationDuration]]]], hourlyBillingFlag, managedResourceFlag, " \
             "operatingSystem[averageInstallationDuration, passwords[sshKeys]], primaryIpAddress, " \
             "softwareComponents[softwareLicense[softwareDescription[features[keyName], " \
             "productItems[categories[categoryCode, name]]]]], networkGatewayMemberFlag]"

failedServers = []
for ipToReload in ipsToReload:
    failedServer = {'ip': ipToReload}
    try:
        server = hardwareService.findByIpAddress(ipToReload, mask=objectMask)
        if server == '':
            failedServer['error'] = "Ip does not exist."
            failedServers.append(failedServer)
            continue
    except SoftLayer.SoftLayerAPIError as e:
        failedServer['error'] = e
        failedServers.append(failedServer)
        continue
    if 'activeTransaction' in server:
        failedServer['error'] = "There is an active transaction."
        failedServers.append(failedServer)
        continue
    priceOs = get_price(server, newOSToLoad)
    priceOsAddom = get_price(server, newOsAddom)
    pricePanel = get_price(server, newControlPanel)
    priceDataBase = get_price(server, newDatabase)
    priceAntivir = get_price(server, newAntivir)
    priceFirewall = get_price(server, newFirewall)
    itemPrices = []
    if priceOs != '':
        itemPrices.append(priceOs)
    if priceOsAddom != '':
        itemPrices.append(priceOsAddom)
    if pricePanel != '':
        itemPrices.append(pricePanel)
    if priceDataBase != '':
        itemPrices.append(priceDataBase)
    if priceAntivir != '':
        itemPrices.append(priceAntivir)
    if priceFirewall != '':
        itemPrices.append(priceFirewall)

    config = {
        'itemPrices': itemPrices,
        'resetIpmiPassword': resetIpmiPassword,
        'upgradeBios': upgradeBios,
        'upgradeHardDriveFirmware': upgradeHardDriveFirmware
    }

    if customProvisionScriptUri != '':
        config['customProvisionScriptUri'] = customProvisionScriptUri

    if len(hardDrives) > 0:
        config['hardDrives'] = hardDrives

    try:
        reload = hardwareService.reloadOperatingSystem('FORCE', config, id=server['id'])
        print('Se inició el proceso de Os Reload')
        print(reload)
    except SoftLayer.SoftLayerAPIError as e:
        failedServer['error'] = e
        failedServers.append(failedServer)
        continue

    print("The reload failed for these IPs:")
    print(json.dumps(failedServers, sort_keys=True, indent=2, separators=(',', ': ')))



```
