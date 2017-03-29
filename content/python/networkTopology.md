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
            mask[attachedNetworkGateway[publicVlan,privateVlan],hardware[fullyQualifiedDomainName],
            network,networkSpace,primaryRouter[hostname],primarySubnet,subnets[networkIdentifier],virtualGuests[fullyQualifiedDomainName]
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
                                        print("\t\t\t\t%s" % hardware['fullyQualifiedDomainName'])
                                if len(orderedVlans[dc][router][vlan][vlanInner]['virtualGuests']):
                                    print("\t\t\t  ==VIRTUAL SERVERS==")
                                    for virtualGuest in orderedVlans[dc][router][vlan][vlanInner]['virtualGuests']:
                                        print("\t\t\t\t%s" % virtualGuest['fullyQualifiedDomainName'])
                                if len(orderedVlans[dc][router][vlan][vlanInner]['subnets']):
                                    print("\t\t\t  ==SUBNETS==")
                                    for subnet in orderedVlans[dc][router][vlan][vlanInner]['subnets']:
                                        print("\t\t\t\t%s" % subnet['networkIdentifier'])
                    else:
                        print("\t\tVLAN: %s" % vlan )

                    if len(orderedVlans[dc][router][vlan]['hardware']):
                        print("\t\t  ==SERVERS==")
                        for hardware in orderedVlans[dc][router][vlan]['hardware']:
                            print("\t\t\t%s" % hardware['fullyQualifiedDomainName'])
                    if len(orderedVlans[dc][router][vlan]['virtualGuests']):
                        print("\t\t  ==VIRTUAL SERVERS==")
                        for vm in orderedVlans[dc][router][vlan]['virtualGuests']:
                            print("\t\t\t%s" % vm['fullyQualifiedDomainName'])
                    if len(orderedVlans[dc][router][vlan]['subnets']):
                        print("\t\t  ==SUBNETS==")
                        for subnet in orderedVlans[dc][router][vlan]['subnets']:
                            print("\t\t\t%s" % subnet['networkIdentifier'])


if __name__ == "__main__":
    main = example()
    main.main()

```

Example Output:
```
DC: sjc03
    Router: bcr02a
        VLAN: 904
          ==VIRTUAL SERVERS==
            jrh-jump.poc.engineering
          ==SUBNETS==
            10.168.140.0
    Router: bcr01a
        GATEWAY VLAN: 1436
            VLAN: 1440
              ==SERVERS==
                jd-test-5600-srv.secore.com
                jd-cos-testing-sjc03.secore.com
              ==SUBNETS==
                10.161.111.64
          ==SERVERS==
            jd-5600-test.secore.com
          ==SUBNETS==
            10.161.110.0
    Router: fcr02a
        VLAN: 857
          ==VIRTUAL SERVERS==
            jrh-jump.poc.engineering
          ==SUBNETS==
            169.44.183.224
    Router: fcr01a
        VLAN: 1296
          ==SERVERS==
            jd-test-5600-srv.secore.com
            jd-cos-testing-sjc03.secore.com
          ==SUBNETS==
            169.45.115.16
            2607:f0d0:2601:00cc:0000:0000:0000:0000
        VLAN: 1273
          ==SERVERS==
            jd-5600-test.secore.com
          ==SUBNETS==
            169.44.136.64
            2607:f0d0:2601:0065:0000:0000:0000:0000
            2607:f0d0:2601:00ac:0000:0000:0000:0000
```
