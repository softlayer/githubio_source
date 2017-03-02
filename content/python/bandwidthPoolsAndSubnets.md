---
title: "Subnets and Bandwidth Pools"
description: "An example of getting information on portable subnets and servers in a bandwidth pool."
date: "2017-02-16"
classes: ["SoftLayer_Account", "SoftLayer_Network_Bandwidth_Version1_Allotment", "SoftLayer_Network_Subnet"]
tags:
    - "objectMask"
    - "objectFilter"
    - "subnet"
    - "bandwidth pool"
---


```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def getPublicSubnets(self):
        """
        subnet types
        SECONDARY_ON_VLAN = Portable IPs
        PRIMARY
        SUBNET_ON_VLAN = static subnets
        PRIMARY_6
        STATIC_IP_ROUTED
        GLOBAL_IP
        ADDITIONAL_PRIMARY
        """
        object_filter = {
            'publicSubnets' : {
                'subnetType' : {
                    'operation': 'SECONDARY_ON_VLAN'
                }
            }
        }

        subnets = self.client['Account'].getPublicSubnets(filter=object_filter)
        pp(subnets)

    def getBandwidthPools(self):
        """
        bareMetalInstances and privateNetworkOnlyHardware
        may need to be included in the mask if applicable. 
        """
        mask = "mask[hardware,virtualGuests]"
        pool = self.client['Account'].getVirtualDedicatedRacks(mask=mask)
        pp(pool)


if __name__ == "__main__":
    main = example()
    main.getBandwidthPools()
    main.getPublicSubnets()
```


