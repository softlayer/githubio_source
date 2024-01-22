---
title: "Update Firmware"
description: "An explanation of how to update the firmware on a bare metal server using the Python SDK."
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "server"
---

This example shows how to update the firmware on a given server. Primarily this script calls [SoftLayer_Hardware_Server::createFirmwareUpdateTransaction](/reference/services/SoftLayer_Hardware_Server/createFirmwareUpdateTransaction/), which has options for what specific bits of firmware you want to update. Currently you can choose to update the following:
- IPMI
- Raid Controller
- BIOS
- Hard Drives
- Network Card


*NOTE* The server will need to be offline for about 20 minutes this update to happen, so be aware of that.

*NOTE* The [`slcli hardware update-firmware`](https://softlayer-python.readthedocs.io/en/latest/cli/hardware/#hardware-update-firmware) and [`ibmcloud sl hardware update-firmware`](https://cloud.ibm.com/docs/cli?topic=cli-sl-manage-bare-metal#sl_hardware_update_firmware) commands have this feature as well. Although they simply update all firmware and do not allow for selecting a specific bit to update.

## Example

```python
"""
@author Christopher Gallo

Updates the firmware of the specified serverid. Server must be offline to be updated.
Script requried
Python 3.7+
click 8.0+  - For making this script a CLI command easily
rich  - To make the output look nice
"""

# Click is used to make this script support CLI arguments
import click
# Used for details table output
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
from rich.live import Live
from rich import print
# The SoftLayer SDK
import SoftLayer
# Used for time.sleep() to wait for a server to power off
import time


class SLSDK():
    """Class used to manage making API calls to the SL API"""
    def __init__(self):
        """SoftLayer Client Initialization"""
        self.client = SoftLayer.Client()
        # This part allows printing out the exact API calls used
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def resolveServerId(self, serverid: int) -> str:
        """Gets the Fully Qualified Domain Name for a server"""
        fqdnMask = "mask[id,fullyQualifiedDomainName]"
        fqdn = self.client.call('SoftLayer_Hardware_Server', 'getObject', id=serverid, mask=fqdnMask)
        return fqdn.get('fullyQualifiedDomainName', '')

    def powerOff(self, serverid: int) -> None:
        """Powers off serverid"""
        self.client.call('SoftLayer_Hardware_Server', 'powerOff', id=serverid)

    def powerOn(self, serverid: int) -> None:
        """Powers on serverid"""
        self.client.call('SoftLayer_Hardware_Server', 'powerOn', id=serverid)

    def update(self, serverid: int, ipmi: bool, raid: bool, bios: bool, harddrive: bool, network: bool) -> bool:
        """Updates firmware for serverID for the specified devices"""
        result = self.client.call('SoftLayer_Hardware_Server', 'createFirmwareUpdateTransaction',
                                  ipmi, raid, bios, harddrive, network, id=serverid)
        return result


def waitForReboot(seconds: int) -> str:
    return f"Wait {seconds} for server to reboot..."

@click.command()
@click.argument('serverid')
@click.option('-f', '--force', is_flag=True, help="Skips the confirmation dialog prompts")
@click.option('-i', '--ipmi', is_flag=True, help="Update IPMI firmware")
@click.option('-r', '--raid', is_flag=True, help="Update RAID firmware")
@click.option('-b', '--bios', is_flag=True, help="Update BIOS firmware")
@click.option('-d', '--harddrive', is_flag=True, help="Update Hard Drives firmware")
@click.option('-n', '--network', is_flag=True, help="Update Network Card firmware")
def updateFirmware(serverid, force, ipmi, raid, bios, harddrive, network):
    # init the SDK Class
    sdk = SLSDK()
    # Take the serverId and get a FQDN from it
    try:
        fqdn = sdk.resolveServerId(serverid)
    except SoftLayer.SoftLayerError as e:
        print(f"[red]Failed to get server [underline]{serverid}[/underline]. Error: [underline]{e}[/underline]")
        raise click.Abort()

    # Make sure the user knows what is about to happen to their server
    if not force:
        prompt = f"You are about to reboot server [red]{fqdn}[/red] and update its firmware, continue?"
        if not Confirm.ask(prompt):
            raise click.Abort()

    # Shutdown the server, wait a few seconds for that to processes
    print(f"Shutting down and updating [red]{fqdn}[/red] now...")
    sdk.powerOff(serverid)
    waitFor = 15
    # This bit is just to be fancy and have an update-in-place counter
    with Live(waitForReboot(waitFor), refresh_per_second=1) as live:
        for second in range(waitFor):
            time.sleep(1)
            live.update(waitForReboot(waitFor - second))

    # Actually do the firmware update. This might return an exception if no firmwares were requested to be udpated.
    try:
        sdk.update(serverid, ipmi, raid, bios, harddrive, network)
        print(f"[green]Successfully updated [underline]{fqdn}[/underline]")
    except SoftLayer.SoftLayerError as e:
        print(f"[red]Failed to update server [underline]{fqdn}[/underline]. Error: [underline]{e}[/underline]")
        raise click.Abort()


if __name__ == "__main__":
    updateFirmware()
```



## Output

```
$> python testFirmwareUpdate.py 3332650 -f -i -r -b -d -n
Calling: SoftLayer_Hardware_Server::getObject(id=3332650, mask='mask[id,fullyQualifiedDomainName]', filter='None', args=(), limit=None, offset=None)
Shutting down and updating ibmtesttest01.ibmtest.com now...
Calling: SoftLayer_Hardware_Server::powerOff(id=3332650, mask='', filter='None', args=(), limit=None, offset=None)
Wait 1 for server to reboot...
Calling: SoftLayer_Hardware_Server::createFirmwareUpdateTransaction(id=3332650, mask='', filter='None', args=(True, True, True, True, True), limit=None, offset=None)
Successfully updated ibmtesttest01.ibmtest.com
```