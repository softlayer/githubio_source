---
title: "scale_group_details_configuration.py"
description: "scale_group_details_configuration.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Policy_Trigger_Repeating"
    - "SoftLayer_Scale_Policy_Trigger_OneTime"
    - "SoftLayer_Scale_Group"
    - "SoftLayer_Scale_Policy_Trigger_ResourceUse"
tags:
    - "scalegroups"
---


```
"""
Get the scale group details (configuration).

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

scaleGroupId = 595465

# Create a SoftLayer API client object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
scaleGroupService = client['SoftLayer_Scale_Group']

objectMask = "mask[id, name, status[name, keyName], regionalGroup[id, name, description], suspendedFlag, terminationPolicy, cooldown, regionalGroupId, minimumMemberCount, maximumMemberCount, balancedTerminationFlag, networkVlans[ id, networkVlan[ id, name, vlanNumber, networkSpace, primaryRouter[id,hostname,datacenter[name,longName]],localDiskStorageCapabilityFlag,sanStorageCapabilityFlag]],virtualGuestMemberTemplate[hostname,domain,fullyQualifiedDomainName,startCpus,maxMemory,hourlyBillingFlag,localDiskFlag,operatingSystem,datacenter,privateNetworkOnlyFlag,networkComponents.maxSpeed,sshKeys,operatingSystemReferenceCode,blockDevices[device,diskImage.capacity],blockDeviceTemplateGroup.globalIdentifier,postInstallScriptUri],policies[id,cooldown,name,scaleActions[id,type[id,keyName,name],amount,scaleType],triggers[id,type],triggers(SoftLayer_Scale_Policy_Trigger_OneTime)[date],triggers(SoftLayer_Scale_Policy_Trigger_Repeating)[schedule],triggers(SoftLayer_Scale_Policy_Trigger_ResourceUse)[watches[id,algorithm,metric,operator,period,value]]],loadBalancers[id,port,healthCheck[id,attributes[value,type.keyname],type[id,keyname,name]],virtualServer[id,port,virtualIpAddress.ipAddress.ipAddress,virtualIpAddress.id,serviceGroups.routingType.name]],virtualGuestMemberCount]"

try:
    scaleGroup = scaleGroupService.getObject(id=scaleGroupId, mask=objectMask)
    config = {}
    config['groupDetails'] = {}
    config['groupDetails']['groupName'] = scaleGroup['name']
    config['groupDetails']['region'] = scaleGroup['regionalGroup']['name']
    config['groupDetails']['datacenter'] = scaleGroup['regionalGroup']['name']
    config['groupDetails']['terminationPolicy'] = scaleGroup['terminationPolicy']['name']
    config['groupSettings'] = {}
    config['groupSettings']['minimumMemberCount'] = scaleGroup['minimumMemberCount']
    config['groupSettings']['maximumMemberCount'] = scaleGroup['maximumMemberCount']
    config['groupSettings']['cooldown'] = str(scaleGroup['cooldown'] / 60) + " Minutes"
    config['memberDetails'] = {}
    config['memberDetails']['hostname'] = scaleGroup['virtualGuestMemberTemplate']['hostname']
    config['memberDetails']['domain'] = scaleGroup['virtualGuestMemberTemplate']['domain']
    config['computingInstance'] = {}
    config['computingInstance']['cores'] = str(scaleGroup['virtualGuestMemberTemplate']['startCpus']) + "x 2.0 GHz Core"
    config['computingInstance']['ram'] = str(scaleGroup['virtualGuestMemberTemplate']['maxMemory'] / 1024) + "GB"
    if 'networkComponents' in scaleGroup['virtualGuestMemberTemplate']:
        config['computingInstance']['speed'] = scaleGroup['virtualGuestMemberTemplate']['networkComponents'][0]['maxSpeed']
    else:
        config['computingInstance']['speed'] = "Default"
    if 'sshKeys' in scaleGroup['virtualGuestMemberTemplate']:
        config['computingInstance']['sshKeys'] = scaleGroup['virtualGuestMemberTemplate']['sshKeys']
    else:
        config['computingInstance']['sshKeys'] = 'None'
    config['storage'] = {}
    if scaleGroup['virtualGuestMemberTemplate']['localDiskFlag']:
        config['storage']['selectedStorage'] = 'Local Storage'
    else:
        config['storage']['selectedStorage'] = 'SAN Storage'
    config['operatingSystem'] = {}
    config['operatingSystem']['selectedOperatingSystem'] = scaleGroup['virtualGuestMemberTemplate']['operatingSystemReferenceCode']
    config['postInstallScript'] = {}
    config['postInstallScript']['url'] = scaleGroup['virtualGuestMemberTemplate']['postInstallScriptUri']
    config['policies'] = scaleGroup['policies']
    print(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the scale group details. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
