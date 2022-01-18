---
title: "Hardware components and versions"
description: "Example on how to get hardware components and versions"
date: "2021-04-27"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "hardware"
    - "server"
    - "ipmi"
    - "raid"
---

This python script contains the following:

1.- Getting hardware information.

2.- Getting the hardware components.

3.- Getting hardware components firmware version information.

4.- Updating the firmware on components.

```python

import SoftLayer
import click
from prettytable import PrettyTable


class HardwareComponents():

    def __init__(self):
        
        self.client = SoftLayer.create_client_from_env()

    def hardware_information(self, hostname):
        """
        Get the Hardware Server Information.
        """
        mask = 'mask[hardwareStatus,lastOperatingSystemReload,datacenter,billingItem[hourlyFlag],' \
               'lastTransaction[transactionGroup],processorPhysicalCoreAmount,memoryCapacity,' \
               'operatingSystem[softwareLicense[softwareDescription]]]'
        hardware_id = self.get_hardware_detail(hostname).get('id')
        result = self.client['SoftLayer_Hardware_Server'].getObject(id=hardware_id, mask=mask)

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

    def list_hardware_components(self, hostname):
        """
        Get the Hardware Server Components.
        """
        mask = 'mask[activeComponents[hardwareComponentModel[hardwareGenericComponentModel[hardwareComponentType]]]]'
        hardware_id = self.get_hardware_detail(hostname).get('id')
        result = self.client['SoftLayer_Hardware_Server'].getObject(id=hardware_id, mask=mask)

        table = PrettyTable()
        table.title = "Hardware Components"
        table.field_names = ['id', 'hardwareComponentType', 'capacity', 'manufacturer', 'name', 'version']

        capacity = None
        component_type = None
        for component in result['activeComponents']:
            if 'hardwareGenericComponentModel' in component['hardwareComponentModel']:
                capacity = component['hardwareComponentModel']['hardwareGenericComponentModel']['capacity']
                component_type = component['hardwareComponentModel']['hardwareGenericComponentModel'][
                    'hardwareComponentType']['type']
                table.add_row([component['hardwareComponentModel']['id'],
                               component_type,
                               capacity,
                               component['hardwareComponentModel']['manufacturer'],
                               component['hardwareComponentModel']['name'],
                               component['hardwareComponentModel']['version']
                               ])

        print(table)

    def list_hardware_component_firmware(self, hostname, component_id=None):
        """
        Get the last firmware version updated for a specific hardware component.
        """
        mask = 'mask[hardwareComponentModel[firmwares]]'
        hardware_id = self.get_hardware_detail(hostname).get('id')

        if component_id:
            result = self.client['SoftLayer_Hardware_Server'].getComponents(mask=mask, id=hardware_id)

            table = PrettyTable()
            table.title = "Hardware Component Firmware"
            table.field_names = ['id', 'createDate', 'hardwareComponentModelId', 'version']

            list_firmware = list()
            for component in result:
                if component_id == component['hardwareComponentModel']['id']:
                    for firmware in component['hardwareComponentModel']['firmwares']:
                        list_firmware.append(firmware)

            if not len(list_firmware) == 0:
                list_result = sorted(list_firmware, key=lambda x: x['createDate'])
                last_firmware = list_result[len(list_result) - 1]
                table.add_row([last_firmware['id'],
                               last_firmware['createDate'],
                               last_firmware['hardwareComponentModelId'],
                               last_firmware['version'],
                               ])

            print(table)
        else:
            print('The hardware component id is required.')

    def update_firmware(self, hostname, ipmi=0, raid_controller=0, bios=0, hard_drive=0):
        """
        Firmware Update.
        """
        result = None
        try:
            hardware_id = self.get_hardware_detail(hostname).get('id')
            result = self.client['SoftLayer_Hardware_Server'].createFirmwareUpdateTransaction(ipmi, 
                                                                                              raid_controller,
                                                                                              bios,
                                                                                              hard_drive,
                                                                                              id=hardware_id)
        except SoftLayer.SoftLayerAPIError as e:
            print("Update failed. faultCode=%s, faultString=%s" % (
                e.faultCode, e.faultString))

        if result:
            print("Update firmware successfully")
        else:
            print("Update firmware failed")

    def get_hardware_detail(self, hostname):
        """
        Get an specific hardware server detail from the account through the hostname.
        """
        object_filter = {
            "hardware": {
                "hostname": {
                    "operation": hostname
                }
            }
        }
        user_detail = self.client['SoftLayer_Account'].getHardware(filter=object_filter)

        return user_detail[0]


@click.command()
@click.argument('hostname')
@click.option('--component-id', type=click.INT,
              help='Hardware Component Id')
@click.option('--ipmi', type=click.INT,
              help='Set this hardware Component to 1 (to upgrade) or 0 (not upgrade)')
@click.option('--raid-controller', type=click.INT,
              help='Set this hardware Component to 1 (to upgrade) or 0 (not upgrade)')
@click.option('--bios', type=click.INT,
              help='Set this hardware Component to 1 (to upgrade) or 0 (not upgrade)')
@click.option('--hard_drive', type=click.INT,
              help='Set this hardware Component to 1 (to upgrade) or 0 (not upgrade)')
def main(hostname, component_id, ipmi, raid_controller, bios, hard_drive):
    main = HardwareComponents()
    # Uncomment this to print out the API calls made.
    """
    Hardware Server Detail.
    """
    # main.hardware_information(hostname)

    """
    Hardware Server Components.
    """
    # main.list_hardware_components(hostname)

    """
    Show the last firmware version updated for a specific hardware component.
    Get the component_id from the second request.
    """
    # main.list_hardware_component_firmware(hostname, component_id=component_id)

    """
    Update Firmware.
    Set the options impi, raid-controller, bios or hard-drive with "1" if you 
    want to update the component or "0" if you do not want to update.
    """
    main.update_firmware(hostname, ipmi=ipmi, raid_controller=raid_controller, bios=bios, hard_drive=hard_drive)


if __name__ == "__main__":
    main()

```
