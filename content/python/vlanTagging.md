---
title: "Tag Vlans"
description: "Some examles of how to add vlans to a server. AKA Vlan Trunks."
date: "2017-06-09"
classes: 
    - "SoftLayer_Network_Component"
tags:
    - "vlan"
    - "server"
---

A rough examples of how to add vlans to servers


*NOTE* When trying to get the vlan tags/trunks from a server, the trunk information is on the `Hardware_Server->networkComponent->uplinkComponent->vlanTrunks` relationship. 
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
