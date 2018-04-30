---
title: "get_gateway_details.py"
description: "get_gateway_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
"""
Get gateway details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getPossibleInsideVlans
http://sldn.softlayer.com/article/object-masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

gatewayId = 61522

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
gatewayService = client['SoftLayer_Network_Gateway']

objectMask = "mask[id, name, networkSpace, status.name, groupNumber, publicIpAddress.ipAddress, privateIpAddress.ipAddress, publicIpv6Address.ipAddress, publicVlan[id, vlanNumber, primaryRouter.hostname, networkSpace], privateVlan[id, vlanNumber, primaryRouter.hostname, networkSpace], members[priority, hardware[id, fullyQualifiedDomainName, primaryIpAddress, primaryBackendIpAddress, primaryNetworkComponent.primaryVersion6IpAddressRecord.ipAddress, operatingSystem[id, passwords[username, password]]]], insideVlans[id, bypassFlag, networkVlan[id, vlanNumber, primaryRouter.hostname, networkSpace]]]"
objectMaskPossibleVlans = "mask[id, vlanNumber, primaryRouter.hostname, networkSpace]"


try:
    details = {}
    gateway = gatewayService.getObject(id=gatewayId, mask=objectMask)
    possibleVlans = gatewayService.getPossibleInsideVlans(id=gatewayId, mask=objectMaskPossibleVlans)
    details['name'] = gateway['name']
    details['network'] = gateway['networkSpace']
    details['publicGatewayIp'] = gateway['publicIpAddress']['ipAddress']
    details['privateGatewayIp'] = gateway['privateIpAddress']['ipAddress']
    details['publicGatewayIpv6'] = gateway['publicIpv6Address']['ipAddress']
    details['groupNumber'] = gateway['groupNumber']
    details['status'] = gateway['status']['name']
    members = []
    for men in gateway['members']:
        member = {}
        member['name'] = men['hardware']['fullyQualifiedDomainName']
        member['id'] = men['hardware']['id']
        member['manageGateway'] = men['hardware']['primaryBackendIpAddress']
        member['publicIp'] = men['hardware']['primaryIpAddress']
        member['publicIpv6'] = men['hardware']['primaryNetworkComponent']['primaryVersion6IpAddressRecord']['ipAddress']
        members.append(member)
    details['members'] = members
    details['vlans'] = []
    details['vlans'].append(gateway['privateVlan'])
    details['vlans'].append(gateway['publicVlan'])
    details['associateVlans'] = gateway['insideVlans']
    details['vlansToAdd'] = possibleVlans
    print(json.dumps(details, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the gateway. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
