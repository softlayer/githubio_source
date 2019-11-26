---
title: "Bandwidth Pools"
description: "An example of getting information on portable subnets and servers in a bandwidth pool."
date: "2017-02-16"
classes:
    - "SoftLayer_Account"
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
    - "SoftLayer_Network_Bandwidth_Version"
    - "SoftLayer_Network_Subnet"
tags:
    - "objectMask"
    - "objectFilter"
    - "subnet"
    - "bandwidthpools"
---

### [VDR](reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/)

SoftLayer allotments are a collection of servers that share all of the servers allocated bandwidth together.


```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

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

    def updatePool(self, pool_id, add_hardware=[], del_hardware=[],
                   add_guest=[], del_guest=[]):
        """
            pool_id is the id from getVirtualDedicatedRacks
            the add/remove hardware/guest are lists IP strings.  
        """
        to_do = ('add_hardware', 'del_hardware', 'add_guest', 'del_guest')
        # Ordered parameters for requestVdrContentUpdates
        params = [[],[],[],[]]
        index = 0
        # Iterate through each parameter
        for arg in to_do:
            ips = locals()[arg]
            # Iterate through each IP
            for ip in ips:
                if 'hardware' in arg:
                    server = self.client.call('SoftLayer_Hardware_Server', 'findByIpAddress', ip)
                else:
                    server = self.client.call('SoftLayer_Virtual_Guest', 'findByIpAddress', ip)
                # If we found a server, add it to the params list
                if server:
                    params[index].append(server)
                else:
                    print("Couldn't find %s", ip)
            index = index + 1
        # At a minimum, we need to send in {'id': XXXX}, but we can send the whole server object in as well.
        result = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'requestVdrContentUpdates',
                                  params[0], params[1], params[2], params[3], id=pool_id)
        pp(result)

    def createPool(self):
        template = {
            "accountId": 123456,
            "bandwidthAllotmentTypeId": 2, # Type 2 is the default
            "locationGroupId": 1,  # The region for the pool.
            "name": "testPoolApi"
        }
        result = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'createObject', template)
        pp(result)

    def printPoolServerDetails(self, pool_id):
        """Prints out info about Hardware_Server in a specific pool"""
        objectMask = "mask(SoftLayer_Hardware_Server)[projectedPublicBandwidthUsage, datacenter, outboundPublicBandwidthUsage, bandwidthAllocation, virtualRackId]"
        objectFilter = {"hardware": {"virtualRackId": {"operation": pool_id}}}
        # For virtual guests
        # objectFilter = {"virtualGuests": {"virtualRackId": {"operation": poolId}}}
        servers = self.client.call('SoftLayer_Account', 'getHardware', mask=objectMaks, filter=objectFilter)
        for server in servers:
            detail = {}
            detail['server'] = server['fullyQualifiedDomainName']
            detail['ip'] = server['primaryIpAddress']
            detail['location'] = server['datacenter']['longName']
            detail['allocation'] = str(float(server['bandwidthAllocation']) / 1000) + " TB"
            detail['currentUsage'] = str(float(server['outboundPublicBandwidthUsage']) * 1000) + " MB"
            detail['projectedUsage'] = str(float(server['projectedPublicBandwidthUsage']) * 1000) + " MB"
            details.append(detail)
        print(json.dumps(details, sort_keys=True, indent=2, separators=(',', ': ')))

    def getVDRLocations(self):
        """Get lists of locations where you can setup a VDR"""
        objectFilter = {"locationGroupType": {"name": {"operation": "VDR"}}}
        locations = self.client.call('SoftLayer_Location_Group', 'getAllObjects', filter=objectFilter)
        pp(locations)

    def getBandwidthAllotments(self):
        """Very similar to getVirtualDedicatedRacks"""
        objectMask = "mask[id, name, serviceProviderId, locationGroup[name], locationGroup, hardwareCount, privateNetworkOnlyHardwareCount, virtualGuestCount, bareMetalInstanceCount, applicationDeliveryControllerCount, totalBandwidthAllocated, outboundPublicBandwidthUsage, bandwidthAllotmentTypeId, projectedPublicBandwidthUsage]"
        objectFilter = {"bandwidthAllotments": {"bandwidthAllotmentTypeId": {"operation": "!= 1"}}}
        pools = []
        data = self.client.call('SoftLayer_Account', 'getBandwidthAllotments', mask=objectMask, filter=objectFilter)
        for item in data:
            pool = {}
            pool['name'] = item['name']
            pool['region'] = item['locationGroup']['name']
            pool['allocation'] = str(item['totalBandwidthAllocated'] / 1000) + " TB"
            if "outboundPublicBandwidthUsage" in item:
                pool['currentUsage'] = str(float(item['outboundPublicBandwidthUsage']) * 1000) + " MB"
            else:
                pool['currentUsage'] = "0 MB"
            if "projectedPublicBandwidthUsage" in item:
                pool['projectableUsage'] = str(item['projectedPublicBandwidthUsage'] * 1000) + " MB"
            else:
                pool['projectableUsage'] = "0 MB"
            pools.append(pool)
        pp(pools)

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))


if __name__ == "__main__":
    main = example()
    main.getBandwidthPools()
    main.getPublicSubnets()
```


