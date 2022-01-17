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

prints out model numbers of networking equipment that is on route to your servers. could be useful if merged with https://softlayer.github.io/python/networktopology/


```
"""
@author christopher gallo
finds the model number of all networking equipment that is on the way to servers on the account.
"""
import softlayer
from pprint import pprint as pp

class networkmap():

    def __init__(self):

        self.client = softlayer.client()

    def main(self):
        """
        goes through each server, and prints out what networking hardware is upstream
        """
        mask = "mask[id, fullyqualifieddomainname]" 
        servers = self.client['softlayer_account'].gethardware(mask=mask)
        for server in servers:
            print("%s" % (server['fullyqualifieddomainname']))
            server_mask = "mask[backendnetworkcomponents[networkhardware[hardwarechassis]]]" 
            this_server = self.client['softlayer_hardware_server'].getobject(id=server['id'],mask=server_mask)
            for component in this_server['backendnetworkcomponents']:
                print("\t%s%s (%smbps) " % (component['name'], component['port'], component['speed']))
                for uplink in component['networkhardware']:
                    print("\t\t%s - %s - %s" % (uplink['fullyqualifieddomainname'], uplink['hardwarechassis']['name'], uplink['hardwarechassis']['hardwarefunction']['description']))


    def fromthetop(self):
        """
        goes through each dc, and prints out the hierarchy of networking gear
        """
        dc_mask="mask[backendhardwarerouters]"
        dcs = self.client['softlayer_location_datacenter'].getdatacenters()

        for dc in dcs:
            print("%s" % (dc['name']))
            router_mask = "mask[hardwarechassis,downlinkhardware[hardwarechassis,downlinkhardware[hardwarechassis,downstreamservers[id,fullyqualifieddomainname],id,fullyqualifieddomainname]]]"
            backend = self.client['softlayer_location_datacenter'].getbackendhardwarerouters(id=dc['id'],mask=router_mask)
            for router in backend:
                print("\t%s - %s - %s " % (router['hardwarefunction']['description'], router['fullyqualifieddomainname'], router['hardwarechassis']['name']))
                # can be used to print out info on the linecards of the bcr/fcr
                # for component in router['components']:
                    # print("\t\t%s" % (component['hardwarecomponentmodel']['longdescription']))
                try:
                    for down in router['downlinkhardware']:
                        print("\t\t%s - %s " % (down['fullyqualifieddomainname'],down['hardwarechassis']['name']))
                        for down_1 in down['downlinkhardware']:
                            print("\t\t\t%s - %s " % (down_1['fullyqualifieddomainname'],down_1['hardwarechassis']['name']))
                            for server in down_1['downstreamservers']:
                                print("\t\t\t\t%s" % server['fullyqualifieddomainname'])
                except keyerror:
                    print("skipping....")


if __name__ == "__main__":
    main = networkmap()
    # main.main()
    main.fromthetop()

```
