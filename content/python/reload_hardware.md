---
title: "Reload Server Examples"
description: "A variety of ways to perform an OS reload on bare metal servers"
date: "2016-01-28"
classes: 
    - "SoftLayer_Hardware_Server"
    - SoftLayer_Hardware_Component_HardDrive
tags:
    - "reload"
    - "server"
    - "deprecated"
    - "sshkeys"
    - "hardware"
aliases:
    - "/python/reloadcustompartition"
---

This article covers a few ways to reload bare metal servers. This article is marked depreciated because of its use of Flex Image Templates, the other ways to reload operating systems are still valid.

### **List Flex Image Templates**
>Flex Images are depreciated as of 8/7/2017. [SoftLayer Product Lifecycle](https://knowledgelayer.softlayer.com/learning/softlayer-product-life-cycle-policy)

Reloading a hardware server from an image template allows users to restore or reconfigure the server based off a pre-existing Flex Image Template that is associated with the account in use. 

To retrieve the list of available Flex Image Template in the account it is required to use object-filters over the method SoftLayer_Account::getPrivateBlockDeviceTemplateGroups as following

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):        
        # Object-filter which is used to retrieve Flex Images
        _filter = {"privateBlockDeviceTemplateGroups":{"imageTypeKeyName":{"operation":"DISK_CAPTURE"}}}
        
        # object-mask to retrieve only the id and name of the image
        _mask = "mask[id,name]"

        accountService = self.client['Account']
        # Retrieve all Flex Images in the account
        images = accountService.getPrivateBlockDeviceTemplateGroups(filter=_filter, mask=_mask)

        pp(images)
        
if __name__ == "__main__":
    main = example()
    main.main()

```

### **Load Hardware Server from Flex Image Template**
SoftLayer does not perform internal backups of customer devices, so the data in the device cannot be retrieved after the OS Reload is initiated. Back up all data on the device prior to initiating the OS Reload. 

Post Install Script, SSH Keys, Reset IPMI Password, Apply Motherboard BIOS upgrades, Apply firmware updates for all hard drives, etc., are some of the features that can be added in the server configuration, it is recommended to review [Container_Hardware_Server_Configuration](https://softlayer.github.io/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration) in order know which additional features can be added.

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        # ID of server which will be reloaded
        serverId = 102938        
        # Flex Image ID
        imageId = 1234567
        
        sshKey1 = 123
        sshKey2 = 456

        # Build reload configuration        
        config = {
            'imageTemplateId': imageId, 
            'sshKeyIds': [sshKey1, sshKey2]
        }

        output = self.client['Hardware_Server'].reloadOperatingSystem('FORCE', config, id=serverId)

        pp(config)
        print "RESULT\n"
        pp(output)

if __name__ == "__main__":
    main = example()
    main.main()

```

### Reload from a list of IP addresses
```python
"""
Reload servers from a list of IPs

This script looks for a server with a determinate IP address and reloads
the Operative System with another one.

It makes a single call to the reloadOperatingSystem() method in the
SoftLayer_Hardware_Server API service

Important manual pages:
https://softlayer.github.io/reference/datatypes/SoftLayer_Hardware_Server
https://softlayer.github.io/reference/services/SoftLayer_Hardware_Server/findByIpAddress
https://softlayer.github.io/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem

"""
import SoftLayer

# The IP addresses you wish to reload
ipsToReload = ['159.8.52.190']

# The new OS you wish to load
newOSToLoad = 'CentOS 6.x - Minimal Install (64 bit)'


# Declare a new API service objects for: SoftLayer_Hardware_Server
client = SoftLayer.create_client_from_env()
hardwareService = client['SoftLayer_Hardware_Server']

"""
Add an object mask to retrieve our prices related to the servers
https://softlayer.github.io/reference/datatypes/SoftLayer_Hardware_Server
for a list of the relational properties you can retrieve along with hardware.
"""
objectMask = "mask[billingItem[package[items[prices]]]]"

# the list of servers to reload
serversToReload = {}

"""
We are looking for the server with the specified IP addresses
and the price for the new OS to load
"""
try:
    for ipToReload in ipsToReload:
        server = hardwareService.findByIpAddress(ipToReload, mask=objectMask)
        serversToReload[ipToReload] = {}
        serversToReload[ipToReload]['id'] = server['id']
        if 'billingItem' in server.keys():
            for item in server["billingItem"]["package"]["items"]:
                if item['description'] == newOSToLoad:
                    serversToReload[ipToReload]['priceId'] = item['prices'][0]['id']
                    break
    # we are calling the reloadOperatingSystem for the desired servers
    for ipToReload in ipsToReload:
        config = {
            'itemPrices': [
                {
                    'id': serversToReload[ipToReload]['id']
                }
                ]
            }
        reload = hardwareService.reloadOperatingSystem('FORCE', config, id=serversToReload[ipToReload]['id'])
        print(reload)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to reload the bare metal servers: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```


### Changing Software options during a reload

```python
"""
Reload servers from a list of IPs, with the option to specify some additional software


Important manual pages:
https://softlayer.github.io/reference/datatypes/SoftLayer_Hardware_Server
https://softlayer.github.io/reference/services/SoftLayer_Hardware_Server/findByIpAddress
https://softlayer.github.io/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem
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

# Partitions for the reload. If you do not want specify partitions set the value empty hardDrives = []
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

client = SoftLayer.create_client_from_env()
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

### Reload with custom partitions

The following code allows you to reload a Bare Metal server with a custom partitioning scheme. You simply need to change the serverId and the partitions to suit your needs. Note that one partition must be marked as the 'grow' partition.

Options for the configuration can be found at the  [SoftLayer_Container_Hardware_Server_Configuration](/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration/) datatype

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        serverId = 1154505
        config = {
        "upgradeHardDriveFirmware": 0,
        "upgradeBios": 0,
        "hardDrives": [
            {
                "complexType": "SoftLayer_Hardware_Component_HardDrive",
                "partitions": [
                    { "name": "/boot", "minimumSize": ".25"},
                    { "name": "/swap0", "minimumSize": "20"},
                    { "name": "/", "minimumSize": "200"},
                    { "name": "/tmp", "minimumSize": "200"},
                    { "name": "/var", "minimumSize": "200"},
                    { "name": "/remove", "minimumSize": "1", "grow": "1"}
                ]
            }
        ],
        "lvmFlag": 0}

        output = self.client['Hardware_Server'].reloadOperatingSystem('FORCE', config, id=serverId)

        pp(config)
        print "RESULT\n"
        pp(output)

if __name__ == "__main__":
    main = example()
    main.main()
```