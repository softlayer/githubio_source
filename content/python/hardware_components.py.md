---
title: "Hardware components and versions"
description: "Example on how to get hardware components and versions"
date: "2021-04-27"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "hardware"
---

This python script contains the following:

1.- Getting hardware information.

2.- Getting the hardware components.

3.- Getting hardware components firmware version information.

4.- Updating the the firmware on components.

```python

import SoftLayer
from prettytable import PrettyTable


class HardwareComponents():

    def __init__(self):

        self.client = SoftLayer.create_client_from_env()

    def hardware_information(self, server_id):
        mask = 'mask[hardwareStatus,lastOperatingSystemReload,datacenter,billingItem[hourlyFlag],' \
               'lastTransaction[transactionGroup],processorPhysicalCoreAmount,memoryCapacity,' \
               'operatingSystem[softwareLicense[softwareDescription]]]'
        result = self.client['SoftLayer_Hardware_Server'].getObject(id=server_id, mask=mask)

        table = PrettyTable()
        table.title = "Hardware Server details"
        table.field_names = ['name', 'value']
        table.align['name'] = 'r'
        table.align['value'] = 'l'

        table.add_row(['Name', result['fullyQualifiedDomainName']])
        table.add_row(['Status', result['hardwareStatus']['status']])
        table.add_row(['Id', result['id']])
        table.add_row(['Started', result['provisionDate']])
        table.add_row(['Reloaded', result['lastOperatingSystemReload']['modifyDate']])
        table.add_row(['MFR Serial #', result['manufacturerSerialNumber']])
        table.add_row(['Location', result['datacenter']['longName']])
        table.add_row(['Serial #', result['serialNumber']])
        table.add_row(['Billing', "Hourly" if result['billingItem']['hourlyFlag'] else "Monthly"])
        table.add_row(['Last transaction', result['lastTransaction']['transactionGroup']['name']])
        table.add_row(['cores', result['processorPhysicalCoreAmount']])
        table.add_row(['memory', result['memoryCapacity']])
        table.add_row(['public_ip', result['primaryIpAddress']])
        table.add_row(['private_ip', result['primaryBackendIpAddress']])
        table.add_row(['os', result['operatingSystem']['softwareLicense']['softwareDescription']['manufacturer']])
        table.add_row(['os_version', result['operatingSystem']['softwareLicense']['softwareDescription']['version']])
        print(table)

    def list_hardware_components(self, server_id):
        mask = 'mask[activeComponents[hardwareComponentModel[hardwareGenericComponentModel[hardwareComponentType]]]]'
        result = self.client['SoftLayer_Hardware_Server'].getObject(id=server_id, mask=mask)

        table = PrettyTable()
        table.title = "Hardware Components"
        table.field_names = ['id', 'capacity', 'manufacturer', 'name', 'version', 'hardwareComponentType']

        capacity = None
        component_type = None
        for component in result['activeComponents']:
            if 'hardwareGenericComponentModel' in component['hardwareComponentModel']:
                capacity = component['hardwareComponentModel']['hardwareGenericComponentModel']['capacity']
                component_type = component['hardwareComponentModel']['hardwareGenericComponentModel'][
                    'hardwareComponentType']['type']
                table.add_row([component['hardwareComponentModel']['id'],
                               capacity,
                               component['hardwareComponentModel']['manufacturer'],
                               component['hardwareComponentModel']['name'],
                               component['hardwareComponentModel']['version'],
                               component_type
                               ])

        print(table)

    def list_hardware_component_firmware(self, server_id, hardware_component_id):
        mask = 'filteredMask[activeComponents[hardwareComponentModel[firmwares]]]'
        object_filter = {
            "hardware": {
                "id": {
                    "operation": server_id
                },
                "activeComponents": {
                    "hardwareComponentModel": {
                        "id": {
                            "operation": hardware_component_id
                        }
                    }
                }
            }
        }

        result = self.client['SoftLayer_Account'].getHardware(mask=mask, filter=object_filter)

        table = PrettyTable()
        table.title = "Hardware Component Firmware"
        table.field_names = ['id', 'createDate', 'hardwareComponentModelId', 'version']

        list_firmware = list()
        for active_component in result:
            for component in active_component['activeComponents']:
                if 'firmwares' in component['hardwareComponentModel']:
                    for firmware in component['hardwareComponentModel']['firmwares']:
                        list_firmware.append(firmware)

        list_result = sorted(list_firmware, key=lambda x: x['createDate'])
        last_firmware = list_result[len(list_result) - 1]
        table.add_row([last_firmware['id'],
                       last_firmware['createDate'],
                       last_firmware['hardwareComponentModelId'],
                       last_firmware['version'],
                       ])

        print(table)

    def update_firmware(self, hardware_id, ipmi=0, raidController=0, bios=0, harddrive=0):
        result = self.client['SoftLayer_Hardware_Server'].createFirmwareUpdateTransaction(ipmi, raidController, bios,
                                                                                          harddrive, id=hardware_id)

        if result:
            print("Update firmware successfully")
        else:
            print("Update firmware failed")


if __name__ == "__main__":
    main = HardwareComponents()

    hardware_id = 1234

    """
    Hardware Server Detail.
    """
    # main.hardware_information(hardware_id)

    """
    Hardware Server Components.
    """
    # main.list_hardware_components(hardware_id)

    """
    Show the last firmware version updated for a specific hardware component.
    Get the component_id from the second request.
    """
    component_id = 1234567
    #main.list_hardware_component_firmware(hardware_id, component_id)

    """
    Update Firmware.
    Set the attributes below with "1" if you want to update the component or "0" if you do not want to update.
    """
    ipmi = 1
    raidController = 1
    bios = 1
    harddrive = 0

    # main.update_firmware(hardware_id, ipmi=ipmi, raidController=raidController, bios=bios, harddrive=harddrive)

```
