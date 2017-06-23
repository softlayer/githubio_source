---
title: "Router Model Map"
description: "Finds the model number of all networking equipment that is on the way to servers on the account."
date: "2017-06-23"
classes:
    - "SoftLayer_Account"
    - "SoftLayer_Location_Datacenter"
    - "SoftLayer_Network"
tags:
    - "network"
    - "locations"
    - "hardware"

--- 

Prints out model numbers of networking equipment that is on route to your servers. Could be useful if merged with https://softlayer.github.io/python/networktopology/


```
"""
@author Christopher Gallo
Finds the model number of all networking equipment that is on the way to servers on the account.
"""
import SoftLayer
from pprint import pprint as pp

class networkMap():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):
        """
        Goes through each server, and prints out what networking hardware is upstream
        """
        mask = "mask[id, fullyQualifiedDomainName]" 
        servers = self.client['SoftLayer_Account'].getHardware(mask=mask)
        for server in servers:
            print("%s" % (server['fullyQualifiedDomainName']))
            server_mask = "mask[backendNetworkComponents[networkHardware[hardwareChassis]]]" 
            this_server = self.client['SoftLayer_Hardware_Server'].getObject(id=server['id'],mask=server_mask)
            for component in this_server['backendNetworkComponents']:
                print("\t%s%s (%smbps) " % (component['name'], component['port'], component['speed']))
                for uplink in component['networkHardware']:
                    print("\t\t%s - %s - %s" % (uplink['fullyQualifiedDomainName'], uplink['hardwareChassis']['name'], uplink['hardwareChassis']['hardwareFunction']['description']))


    def fromTheTop(self):
        """
        Goes through each DC, and prints out the hierarchy of networking gear
        """
        dc_mask="mask[backendHardwareRouters]"
        dcs = self.client['SoftLayer_Location_Datacenter'].getDatacenters()

        for dc in dcs:
            print("%s" % (dc['name']))
            router_mask = "mask[hardwareChassis,downlinkHardware[hardwareChassis,downlinkHardware[hardwareChassis,downstreamServers[id,fullyQualifiedDomainName],id,fullyQualifiedDomainName]]]"
            backend = self.client['SoftLayer_Location_Datacenter'].getBackendHardwareRouters(id=dc['id'],mask=router_mask)
            for router in backend:
                print("\t%s - %s - %s " % (router['hardwareFunction']['description'], router['fullyQualifiedDomainName'], router['hardwareChassis']['name']))
                # Can be used to print out info on the linecards of the BCR/FCR
                # for component in router['components']:
                    # print("\t\t%s" % (component['hardwareComponentModel']['longDescription']))
                try:
                    for down in router['downlinkHardware']:
                        print("\t\t%s - %s " % (down['fullyQualifiedDomainName'],down['hardwareChassis']['name']))
                        for down_1 in down['downlinkHardware']:
                            print("\t\t\t%s - %s " % (down_1['fullyQualifiedDomainName'],down_1['hardwareChassis']['name']))
                            for server in down_1['downstreamServers']:
                                print("\t\t\t\t%s" % server['fullyQualifiedDomainName'])
                except KeyError:
                    print("Skipping....")


if __name__ == "__main__":
    main = networkMap()
    # main.main()
    main.fromTheTop()

```
