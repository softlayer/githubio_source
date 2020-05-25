---
title: "Network Topology"
description: "Prints out a rough topology of your network. 
DC -> Router -> Vlan -> Server, and includes gateways if applicable"
date: "2017-03-17"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Network_Gateway"
tags:
    - "topology"
    - "network"
    - "vlan"
---


```python
"""
@author Christopher Gallo
"""
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()


    def main(self):

        mask = """
            mask[
                attachedNetworkGateway[publicVlan,privateVlan],
                hardware[fullyQualifiedDomainName,frontendNetworkComponents[uplinkComponent], backendNetworkComponents[uplinkComponent]],
                network,
                networkSpace,
                primaryRouter[hostname],
                primarySubnet,
                subnets[networkIdentifier],
                virtualGuests[fullyQualifiedDomainName]
            ]
        """
        orderedVlans = {}
        result = self.client['SoftLayer_Account'].getNetworkVlans(mask=mask)

        """
        This bit builds a nicely structured object of the network topology
        """
        for vlan in result:
            vlanNumber = vlan['vlanNumber']
            router,dc  = vlan['primaryRouter']['hostname'].split(".")
            if dc not in orderedVlans:
                orderedVlans[dc] = {}
            if router not in orderedVlans[dc]:
                orderedVlans[dc][router] = {}


            toAppend = {
                'hardware': vlan['hardware'],
                'virtualGuests': vlan['virtualGuests'],
                'subnets': vlan['subnets']

            }

            if 'attachedNetworkGateway' in vlan:
                if vlan['networkSpace'] == 'PUBLIC':
                    gatewayVlan = vlan['attachedNetworkGateway']['publicVlan']['vlanNumber']
                elif vlan['networkSpace'] == 'PRIVATE':
                    gatewayVlan = vlan['attachedNetworkGateway']['privateVlan']['vlanNumber']
                if gatewayVlan not in orderedVlans[dc][router]:
                    orderedVlans[dc][router][gatewayVlan] = {}
                orderedVlans[dc][router][gatewayVlan][vlanNumber] = toAppend
                orderedVlans[dc][router][gatewayVlan]['gateway'] = True
            else:
                orderedVlans[dc][router][vlanNumber] = toAppend

        """
        This bit prints out everything nicely-ish.
        """
        for dc in orderedVlans:
            print("DC: %s" % dc)
            for router in orderedVlans[dc]:
                print("\tRouter: %s" % router)
                for vlan in orderedVlans[dc][router]:
                    if 'gateway' in orderedVlans[dc][router][vlan]:
                        print("\t\tGATEWAY VLAN: %s" % vlan )
                        for vlanInner in orderedVlans[dc][router][vlan]:

                            if isinstance(vlanInner, int):
                                print("\t\t\tVLAN: %s" % vlanInner )
                                if len(orderedVlans[dc][router][vlan][vlanInner]['hardware']):
                                    print("\t\t\t  ==SERVERS==")
                                    for hardware in orderedVlans[dc][router][vlan][vlanInner]['hardware']:
                                        self.printServer(hardware)
                                if len(orderedVlans[dc][router][vlan][vlanInner]['virtualGuests']):
                                    print("\t\t\t  ==VIRTUAL SERVERS==")
                                    for virtualGuest in orderedVlans[dc][router][vlan][vlanInner]['virtualGuests']:
                                        self.printServer(virtualGuest)
                                if len(orderedVlans[dc][router][vlan][vlanInner]['subnets']):
                                    print("\t\t\t  ==SUBNETS==")
                                    for subnet in orderedVlans[dc][router][vlan][vlanInner]['subnets']:
                                        print("\t\t\t\t%s" % subnet['networkIdentifier'])
                    else:
                        print("\t\tVLAN: %s" % vlan )
                    if len(orderedVlans[dc][router][vlan]['hardware']):
                        print("\t\t  ==SERVERS==")
                        for hardware in orderedVlans[dc][router][vlan]['hardware']:
                            self.printServer(hardware)
                    if len(orderedVlans[dc][router][vlan]['virtualGuests']):
                        print("\t\t  ==VIRTUAL SERVERS==")
                        for vm in orderedVlans[dc][router][vlan]['virtualGuests']:
                            self.printServer(vm)
                    if len(orderedVlans[dc][router][vlan]['subnets']):
                        print("\t\t  ==SUBNETS==")
                        for subnet in orderedVlans[dc][router][vlan]['subnets']:
                            print("\t\t\t%s" % subnet['networkIdentifier'])

    def printServer(self, server):
        print("\t\t\t%s" % server['fullyQualifiedDomainName'])
        # pp(server)
        if 'frontendNetworkComponents'  in server:
            for eth in server['frontendNetworkComponents']:
                switch = eth['uplinkComponent']['hardware']['hostname'] if 'hardware' in eth['uplinkComponent'] else "N.A."
                switch_port = eth['uplinkComponent']['port']
                print("\t\t\t\teth%s => %s:%s " % (eth['port'],switch,switch_port))
        if 'backendNetworkComponents'  in server:
            for eth in server['backendNetworkComponents']:
                switch = eth['uplinkComponent']['hardware']['hostname'] if 'hardware' in eth['uplinkComponent'] else "N.A."
                switch_port = eth['uplinkComponent']['port']
                print("\t\t\t\teth%s => %s:%s " % (eth['port'],switch,switch_port))


if __name__ == "__main__":
    main = example()
    main.main()
```

Example Output:
```
DC: sjc03
    Router: bcr02a
        VLAN: 1253
          ==SERVERS==
            jd-centos-6-5.secore.com
                eth1 => fcs421a.sr01.sjc03:19
                eth3 => fcs421b.sr01.sjc03:19
                eth0 => bcs421a.sr01.sjc03:19
                eth0 => bms421.sr01.sjc03:19
                eth2 => bcs421b.sr01.sjc03:19
          ==VIRTUAL SERVERS==
            CW-SJC.softlayer.com
          ==SUBNETS==
            10.168.30.0
            10.168.174.128
            10.168.174.192
        GATEWAY VLAN: 1310
            VLAN: 1288
              ==SERVERS==
            kramvcs-esx0.vmonic.local
                eth1 => fcs422a.sr01.sjc03:37
                eth3 => fcs422b.sr01.sjc03:37
                eth0 => bcs422a.sr01.sjc03:37
                eth0 => bms422.sr01.sjc03:37
                eth2 => bcs422b.sr01.sjc03:37
            kramvcs-esx1.vmonic.local
                eth1 => fcs422a.sr01.sjc03:40
                eth3 => fcs422b.sr01.sjc03:40
                eth0 => bcs422a.sr01.sjc03:40
                eth0 => bms422.sr01.sjc03:40
                eth2 => bcs422b.sr01.sjc03:40
              ==VIRTUAL SERVERS==
            kramjump.seteam.net
            kramvcsveeam.vmonic.local
            zerto.kramVCS.vmonic.local
              ==SUBNETS==
                10.168.117.128
                10.168.137.128
                10.168.212.128
                10.168.212.192
                10.169.200.64
          ==SERVERS==
            jd-5600-1u-test-2.secore.com
                eth1 => fcs377a.sr01.sjc03:11
                eth3 => fcs377b.sr01.sjc03:11
                eth0 => bcs377a.sr01.sjc03:11
                eth0 => bms377.sr01.sjc03:11
                eth2 => bcs377b.sr01.sjc03:11
            jd-5600-test-sjc03-2.secore.com
                eth1 => fcs487a.sr01.sjc03:20
                eth3 => fcs487b.sr01.sjc03:20
                eth0 => bcs487a.sr01.sjc03:20
                eth0 => bms487.sr01.sjc03:20
                eth2 => bcs487b.sr01.sjc03:20
            jd-5600-1u-test-1.secore.com
                eth1 => fcs390a.sr01.sjc03:6
                eth3 => fcs390b.sr01.sjc03:6
                eth0 => bcs390a.sr01.sjc03:6
                eth0 => bms390.sr01.sjc03:6
                eth2 => bcs390b.sr01.sjc03:6
          ==SUBNETS==
            10.168.63.0
```
