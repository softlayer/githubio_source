---
title: "Trunking VLANs"
description: "Some examles of how to adding VLAN Trunks. AKA VLAN Tagging"
date: "2022-08-04"
classes: 
    - "SoftLayer_Network_Component"
tags:
    - "vlan"
    - "server"
---
This example shows how to add VLAN Trunks to a server.

*NOTE* When trying to get the vlan tags/trunks from a server, the trunk information is on the `Hardware_Server->networkComponent->uplinkComponent->vlanTrunks` relationship. Esentially the Server's NIC doesn't know about network VLANs, but the switch port that is connected to the NIC does.


## VLAN Trunks

```python
"""
@author Christopher Gallo

Adds specified Public and Private VLANs to a given server ID.
Script requried
Python 3.7+
click 8.0+
rich 
"""

# Click is used to make this script support CLI arguments
import click
# Used for details table output
from rich.console import Console
from rich.table import Table

import SoftLayer
from pprint import pprint as pp 

class testVlanTrunk():
    def __init__(self):
        """SoftLayer Client"""
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def trunkPublic(self, serverId, vlans):
        """Adds Trunks to a Public network component"""
        component = self.getNetworkComponents(serverId, private=False)
        networkVlans = self.listToVlan(vlans)
        self.addTrunks(component.get('id'), networkVlans)
       
    def trunkPrivate(self, serverId, vlans):
        """Adds Trunks to a Private network component"""
        component = self.getNetworkComponents(serverId, private=True)
        networkVlans = self.listToVlan(vlans)
        self.addTrunks(component.get('id'), networkVlans)

    def addTrunks(self, component_id, networkVlans, type="Public"):
        """Makes the actual API call to add VLAN Trunks"""
        try:
            # Vlans should be added in a single API call. networkVlans is a list of all the vlans you want added
            self.client.call('Network_Component', 'addNetworkVlanTrunks', networkVlans, id=component_id)
            click.secho(f"VLANs successfully added", fg='green')
        except SoftLayer.exceptions.SoftLayerAPIError as ex:
            click.secho(f"Unable to trunk vlans on the {type} Interface...", fg="red")
            click.secho(f"{ex}", fg="red")

    def getNetworkComponents(self, serverId, private=True):
        """Returns either Private or Public network component for a server"""

        method = 'getPrimaryNetworkComponent'
        if private:
            method = 'getPrimaryBackendNetworkComponent'
        component = self.client.call('SoftLayer_Hardware_Server', method, id=serverId)
        return component

    def getServerDetails(self, serverId):
        """Prints some basic information about the server and its Network Components, VLANs, VLAN Trunks"""
        serverMask = """mask[id,hostname,domain,networkComponents[uplinkComponent[
                        networkVlan,networkVlanTrunks[networkVlan[id,vlanNumber]]]]]"""
        server = self.client.call('SoftLayer_Hardware_Server', 'getObject', id=serverId, mask=serverMask)
        table = Table(title=f"{server.get('hostname')}.{server.get('domain')} Network Components")
        table.add_column("Id")
        table.add_column("Primary IP")
        table.add_column("Primary VLAN")
        table.add_column("VLAN Trunks")
        for component in server.get('networkComponents', []):
            if component.get('primaryIpAddress', False):
                uplink = component.get('uplinkComponent')
                trunks = []
                # Trunk information is stored in the UPLINK component, not the server's component
                for trunk in uplink.get('networkVlanTrunks'):
                    trunk_vlan = trunk.get('networkVlan')
                    trunks.append(str(trunk_vlan.get('vlanNumber')))

                vlan = uplink.get('networkVlan', {})
                # Need to cast everything to string for Rich.Table()
                table.add_row(
                    str(component.get('id')),
                    str(component.get('primaryIpAddress')),
                    str(vlan.get('vlanNumber')), 
                    ", ".join(trunks)
                )
        console = Console()
        console.print(table)

    @staticmethod
    def listToVlan(vlans):
        """converts a list of vlan numbers to SoftLayer_Network_Vlan objects"""
        networkVlans = []
        for vlan in vlans:
            networkVlans.append({'vlanNumber': vlan})
        return networkVlans


@click.command()
@click.argument('serverid')
@click.option('-u', '--public', multiple=True, help="Public VLAN number to add")
@click.option('-i', '--private', multiple=True, help="Private VLAN number to add")
@click.option('-d', '--detail', is_flag=True, help="Shows details of this server's network components")
def trunkVlans(serverid, public, private, detail):
    vlanTrunk = testVlanTrunk()
    if not any([public, private, detail]):
        raise(click.ClickException("Specify at least one VLAN, or --detail"))
    if public:
        vlanTrunk.trunkPublic(serverid, public)
    if private:
        vlanTrunk.trunkPrivate(serverid, private)
    if detail:
        vlanTrunk.getServerDetails(serverid)


if __name__ == "__main__":
    trunkVlans()
```


### Output

```
$ python vlanTaggingExample.py 1403539 --detail --public 997  --private 1325
Calling: SoftLayer_Hardware_Server::getPrimaryNetworkComponent(id=1403539, mask='', filter='None', args=(), limit=None, offset=None))
Calling: SoftLayer_Network_Component::addNetworkVlanTrunks(id=10646647, mask='', filter='None', args=([{'vlanNumber': '997'}],), limit=None, offset=None))
VLANs successfully added
Calling: SoftLayer_Hardware_Server::getPrimaryBackendNetworkComponent(id=1403539, mask='', filter='None', args=(), limit=None, offset=None))
Calling: SoftLayer_Network_Component::addNetworkVlanTrunks(id=10646645, mask='', filter='None', args=([{'vlanNumber': '1325'}],), limit=None, offset=None))
VLANs successfully added
Calling: SoftLayer_Hardware_Server::getObject(id=1403539, mask='mask[id,hostname,domain,networkComponents[uplinkComponent[ networkVlan,networkVlanTrunks[networkVlan[id,vlanNumber]]]]]', filter='None', args=(), limit=None, offset=None))
        bardcabero.testedit.com Network Components
+--------------------------------------------------------+
| Id       | Primary IP     | Primary VLAN | VLAN Trunks |
|----------+----------------+--------------+-------------|
| 10646645 | 10.93.138.202  | 886          | 1325        |
| 10646647 | 169.48.191.244 | 1236         | 997         |
+--------------------------------------------------------+

```


## Old Example

This example was created in 2017 and is kept to show the difference in how the API has changed. In this example, Vlan Trunks are added to the network component in a series of API calls. However it is best to add all VLANs you want in a single API call.
```python
"""
@author Christopher Gallo


@sldn{SoftLayer_Network_Component}
@sldn{SoftLayer_Network_Component,getNetworkVlanTrunks}

@manager{hardware}
Goes through a list of servers, add the specified vlan to each one
"""

import SoftLayer
from pprint import pprint as pp 

class testVlanTag():
    def __init__(self):
        """SoftLayer Client"""
        self.client = SoftLayer.Client()
        self.mgr = SoftLayer.HardwareManager(self.client)    

    def addVlanTrunks(self, id, vlans):
        """
            Adds a vlan to a network component
            @param id ID of SoftLayer_Network_Component you want to add vlan to
            @param vlans dictionary of vlan nubmers you want to add
            @sldn{SoftLayer_Network_Component,addNetworkVlanTrunks}
            @sldn{SoftLayer_Network_Component,getNetworkVlanTrunks}
        """
        for vlanNumber in vlans:
            print "Adding vlan %s to %s" % (vlanNumber,id)
            result = self.client['Network_Component'].addNetworkVlanTrunks([{'vlanNumber':vlanNumber}],id=id)
            vlan = self.client['Network_Component'].getNetworkVlanTrunks(id=id)


    def main(self):
        """
            Runs through a list of server ids and tags them with the proper vlan
            Does both public and private interfaces
        """
        """comma seperated list of ids"""
        serverIds = [14274503]
        """comma seperated list of public vlan nubmers to tag on each server"""
        publicVlanNumbers = [1125,1110]
        """comma seperated list of private vlan nubmers to tag on each server"""
        privateVlanNumbers = [1110]

        for sid in serverIds:
            hardware = self.mgr.get_hardware(sid)
            privateIP = hardware['primaryBackendIpAddress']
            print "Private IP is: %s" % (privateIP) 
            publicIP = hardware['primaryIpAddress']
            print "Public IP is: %s" % (publicIP)

            for component in hardware['networkComponents']:
                try:
                    if (component['primaryIpAddress'] == publicIP):
                        continue
                        # self.addVlanTrunks(component['id'],publicVlanNumbers)
                    elif (component['primaryIpAddress'] == privateIP):
                        self.addVlanTrunks(component['id'],privateVlanNumbers)
                    # result = self.client['Network_Component'].clearNetworkVlanTrunks(id=component['id'])
                    mask = 'networkVlan, networkVlanTrunks, uplinkComponent[networkVlanTrunks]'
                    nic = self.client['Network_Component'].getObject(id=component['id'], mask=mask)
                    pp(nic)
                except KeyError:
                    continue

            print "Done with %s " % (hardware['hostname'])
            print "====================================="  

if __name__ == "__main__":
    main = testVlanTag()
    main.main()
```
