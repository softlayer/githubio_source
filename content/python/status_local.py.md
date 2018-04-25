---
title: "status_local.py"
description: "status_local.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "network"
---


```
"""
Get network status local

The script displays the same information as the https://control.softlayer.com/network/status/local page.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Account/
https://sldn.softlayer.com/reference/services/SoftLayer_Account/getObject
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
"""
import SoftLayer
import json


def getRacks(networkHardware, routerStatus):
    """Retrieves the racks information.
       :param SoftLayer_Hardware networkHardware: A network hardware downstream.
       :param SoftLayer_Hardware routerStatus: The routers in the account which contains the network incidents.
    """
    racks = []
    if 'downstreamNetworkHardware' in networkHardware:
        for network in networkHardware['downstreamNetworkHardware']:
            rack = {}
            if 'cs' in network['hostname']:
                rack['name'] = network['hostname'] + '.' + network['domain']
                rack['type'] = network['hardwareChassis']['hardwareFunction']['code']
                rack['status'] = getAggregationRackStatus(network, routerStatus)
                racks.append(rack)
    return racks


def getAggregationRackStatus(networkHardware, routerStatus):
    """Retrieves the status for racks and aggregation hardware.
       :param SoftLayer_Hardware networkHardware: A network hardware downstream.
       :param SoftLayer_Hardware routerStatus: The routers in the account which contains the network incidents.
    """
    if 'downstreamNetworkHardwareWithIncidents' in routerStatus:
        for incident in routerStatus['downstreamNetworkHardwareWithIncidents']:
            if incident['hostname'] == networkHardware['hostname']:
                return incident['networkStatus']
    else:
        return routerStatus['networkStatus']


def getAggregation(router, routerStatus):
    """Retrieves the racks information.
       :param SoftLayer_Hardware router: A router hardware.
       :param SoftLayer_Hardware routerStatus: The routers in the account which contains the network incidents.
    """
    aggregations = []
    if 'downstreamNetworkHardware' in router:
        for networkHardware in router['downstreamNetworkHardware']:
            aggregation= {}
            if 'as' in networkHardware['hostname']:
                aggregation['name'] = networkHardware['hostname'] + '.' + networkHardware['domain']
                aggregation['type'] = networkHardware['hardwareChassis']['hardwareFunction']['code']
                aggregation['status'] = getAggregationRackStatus(networkHardware, routerStatus)
                aggregation['rack'] = getRacks(networkHardware, routerStatus)
                aggregations.append(aggregation)
    return aggregations


USERNAME = 'set me'
API_KEY = 'set me'

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[id,routers[id,hardwareChassis[manufacturer,name,hardwareFunction[code,description]],hostname,domain,networkStatus,networkMonitorAttachedDownVirtualGuestCount,networkMonitorAttachedDownHardwareCount,downstreamNetworkHardware[downstreamNetworkHardware,hostname,domain,hardwareChassis[manufacturer,name,hardwareFunction[code,description]]]]]"
objectMaskStatus = "mask[networkMonitorDownVirtualGuestCount,networkMonitorDownHardwareCount,routers[downstreamNetworkHardwareWithIncidents[hardwareChassis[hardwareFunction], networkStatus]]]"

try:
    response = accountService.getObject(mask=objectMask)
    responseStatus = accountService.getObject(mask=objectMask)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the account. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))


routers = []
for i in range(0, len(response['routers'])):
    router = response['routers'][i]
    routerStatus = responseStatus['routers'][i]
    device = {}
    device['name'] = router['hostname'] + "." + router['domain']
    device['type'] = router['hardwareChassis']['hardwareFunction']['code']
    device['status'] = router['networkStatus']
    device['aggregation'] = getAggregation(router, routerStatus)
    device['routerstatus'] = routerStatus['id']
    device['id'] = router['id']
    routers.append(device)

print(json.dumps(routers, sort_keys=True, indent=2, separators=(',', ': ')))

```
