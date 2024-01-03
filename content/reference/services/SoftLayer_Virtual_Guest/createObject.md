---
title: "createObject"
description: "
createObject() enables the creation of computing instances on an account. This method is a simplified alternative to interacting with the ordering system directly. 


In order to create a computing instance, a template object must be sent in with a few required values. 


When this method returns an order will have been placed for a computing instance of the specified configuration. 


To determine when the instance is available you can poll the instance via [SoftLayer_Virtual_Guest::getObject](/reference/services/SoftLayer_Virtual_Guest/getObject), with an object mask requesting the `provisionDate` relational property. When `provisionDate` is not `null`, the instance will be ready. 


> **Warning:** Computing instances created via this method will incur charges on your account. For testing input parameters see [SoftLayer_Virtual_Guest::generateOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate). 


### Required Input [SoftLayer_Virtual_Guest](/reference/datatypes/SoftLayer_Virtual_Guest)



- `Hostname`  String **Required** 
    + Hostname for the computing instance. 
- `Domain` String **Required** 
    + Domain for the computing instance. 
- `startCpus` Integer **Required** 
    + The number of CPU cores to allocate. 
    + See [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions) for available options. 
- `maxMemory` Integer **Required** 
    + The amount of memory to allocate in megabytes. 
    + See [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions) for available options. 
- `datacenter.name` *String* **Required** 
    + Specifies which datacenter the instance is to be provisioned in. Needs to be a nested object. 
    + Example: `'datacenter': {'name': 'dal05'}` 
    + See [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions) for available options. 


- `hourlyBillingFlag` Boolean **Required** 
    + Specifies the billing type for the instance. 
    + True for hourly billing, False for monthly billing. 
- `localDiskFlag` Boolean **Required** 
    + Specifies the disk type for the instance. 
    + True for local to the instance disks, False for SAN disks. 
- `dedicatedAccountHostOnlyFlag` Boolean 
    + When true this flag specifies that a compute instance is to run on hosts that only have guests from the same account. 
    + Default: False 
- `operatingSystemReferenceCode` String **Conditionally required** 
    + An identifier for the operating system to provision the computing instance with. 
    + Not required when using a `blockDeviceTemplateGroup.globalIdentifier`, as the template will have its own operating system. 
    + See [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions) for available options. 
    + **Notice**: Some operating systems are billed based on the number of CPUs the guest has. The price which is used can be determined by calling 
           [SoftLayer_Virtual_Guest::generateOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate) with your desired device specifications. 
- `blockDeviceTemplateGroup.globalIdentifier` String 
    + The GUID for the template to be used to provision the computing instance. 
    + Conflicts with `operatingSystemReferenceCode` 
    + **Notice**: Some operating systems are billed based on the number of CPUs the guest has. The price which is used can be determined by calling 
           [SoftLayer_Virtual_Guest::generateOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate) with your desired device specifications. 
    + A list of public images may be obtained via a request to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::getPublicImages](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicImages) 
    + A list of private images may be obtained via a request to [SoftLayer_Account::getPrivateBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups) 
    + Example: `'blockDeviceTemplateGroup': { globalIdentifier': '07beadaa-1e11-476e-a188-3f7795feb9fb'` 
- `networkComponents.maxSpeed` Integer 
    + Specifies the connection speed for the instance's network components. 
    +  The `networkComponents` property is an array with a single [SoftLayer_Virtual_Guest_Network_Component](/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component) structure. 
           The `maxSpeed` property must be set to specify the network uplink speed, in megabits per second, of the computing instance. 
    +  See [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions) for available options. 
    + Default: 10 
    + Example: `'networkComponents': [{'maxSpeed': 1000}]` 
- `privateNetworkOnlyFlag` Boolean 
    + When true this flag specifies that a compute instance is to only have access to the private network. 
    + Default: False 
- `primaryNetworkComponent.networkVlan.id` Integer 
    + Specifies the network vlan which is to be used for the frontend interface of the computing instance. 
    + The `primaryNetworkComponent` property is a [SoftLayer_Virtual_Guest_Network_Component](/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component) structure with the `networkVlan` property populated with a i 
          [SoftLayer_Network_Vlan](/reference/datatypes/SoftLayer_Network_Vlan) structure. The `id` property must be set to specify the frontend network vlan of the computing instance. 
    + *NOTE* This is the VLAN `id`, NOT the vlan number. 
    + Example: `'primaryNetworkComponent':{'networkVlan': {'id': 1234567}}` 
- `backendNetworkComponent.networkVlan.id` Integer 
    + Specifies the network vlan which is to be used for the backend interface of the computing instance. 
    + The `backendNetworkComponent` property is a [SoftLayer_Virtual_Guest_Network_Component](/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component) structure with the `networkVlan` property populated with a 
           [SoftLayer_Network_Vlan](/reference/datatypes/SoftLayer_Network_Vlan) structure. The `id` property must be set to specify the backend network vlan of the computing instance. 
    + *NOTE* This is the VLAN `id`, NOT the vlan number. 
    + Example: `'backendNetworkComponent':{'networkVlan': {'id': 1234567}}` 
- `primaryNetworkComponent.securityGroupBindings` [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding](/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding)[] 
    + Specifies the security groups to be attached to this VSI's frontend network adapter 
    + The `primaryNetworkComponent` property is a [SoftLayer_Virtual_Guest_Network_Component](/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component) structure with the `securityGroupBindings` property populated 
           with an array of [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding](/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding) structures. The `securityGroup` property in each must be set to 
           specify the security group to be attached to the primary frontend network component. 
    + Example: 
        ``` 
        'primaryNetworkComponent': { 
            'securityGroupBindings': [ 
                {'securityGroup':{'id': 5555555}}, 
                {'securityGroup':{'id': 1112223}}, 
            ] 
        } 
        ``` 
- `primaryBackendNetworkComponent.securityGroupBindings` [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding](/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding)[] 
    + Specifies the security groups to be attached to this VSI's backend network adapter 
    + The `primaryNetworkComponent` property is a [SoftLayer_Virtual_Guest_Network_Component](/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component) structure with the `securityGroupBindings` property populated 
           with an array of [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding](/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding) structures. The `securityGroup` property in each must be set to 
           specify the security group to be attached to the primary frontend network component. 
    + Example: 
        ``` 
        'primaryBackendNetworkComponent': { 
            'securityGroupBindings': [ 
                {'securityGroup':{'id': 33322211}}, 
                {'securityGroup':{'id': 77777222}}, 
            ] 
        } 
        ``` 
- `blockDevices` [SoftLayer_Virtual_Guest_Block_Device](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device)[] 
    + Block device and disk image settings for the computing instance 
    + The `blockDevices` property is an array of [SoftLayer_Virtual_Guest_Block_Device](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device) structures. Each block device must specify the `device` property 
          along with the `diskImage`  property, which is a [SoftLayer_Virtual_Disk_Image](/reference/datatypes/SoftLayer_Virtual_Disk_Image) structure with the `capacity` property set. The `device` number `'1'` 
          is reserved for the SWAP disk attached to the computing instance. 
    + Default: The smallest available capacity for the primary disk will be used. If an image template is specified the disk capacity will be be provided by the template. 
    + Example: 
        ``` 
        'blockDevices':[{'device': '0', 'diskImage': {'capacity': 100}}], 
        'localDiskFlag': true 
        ``` 
    +  See [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions) for available options. 
- `userData.value`  String 
    + Arbitrary data to be made available to the computing instance. 
    + The `userData` property is an array with a single [SoftLayer_Virtual_Guest_Attribute](/reference/datatypes/SoftLayer_Virtual_Guest_Attribute) structure with the `value` property set to an arbitrary value. 
          This value can be retrieved via the [SoftLayer_Resource_Metadata::getUserMetadata](/reference/services/SoftLayer_Resource_Metadata/getUserMetadata) method from a request originating from the computing instance. 
          This is primarily useful for providing data to software that may be on the instance and configured to execute upon first boot. 
    + Example: `'userData':[{'value': 'testData'}]` 
- `sshKeys` [SoftLayer_Security_Ssh_Key](/reference/datatypes/SoftLayer_Security_Ssh_Key)[] 
    + The `sshKeys` property is an array of [SoftLayer_Security_Ssh_Key](/reference/datatypes/SoftLayer_Security_Ssh_Key) structures with the `id` property set to the value of an existing SSH key. 
    + To create a new SSH key, call [SoftLayer_Security_Ssh_Key::createObject](/reference/services/SoftLayer_Security_Ssh_Key/createObject). 
    + To obtain a list of existing SSH keys, call [SoftLayer_Account::getSshKeys](/reference/services/SoftLayer_Account/getSshKeys) 
    + Example: `'sshKeys':[{'id': 1234567}]` 
- `postInstallScriptUri` String 
    + Specifies the uri location of the script to be downloaded and run after installation is complete. Only scripts from HTTPS servers are executed on startup. 


REST Example: 
``` 
curl -X POST -d '{ 
    'parameters':[ 
        { 
            'hostname': 'host1', 
            'domain': 'example.com', 
            'startCpus': 1, 
            'maxMemory': 1024, 
            'hourlyBillingFlag': true, 
            'localDiskFlag': true, 
            'operatingSystemReferenceCode': 'UBUNTU_LATEST' 
        } 
}' https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/createObject.json 


HTTP/1.1 201 Created 
Location: https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/1301396/getObject 


{ 
  'accountId': 232298, 
  'createDate': '2012-11-30T16:28:17-06:00', 
  'dedicatedAccountHostOnlyFlag': false, 
  'domain': 'example.com', 
  'hostname': 'host1', 
  'id': 1301396, 
  'lastPowerStateId': null, 
  'lastVerifiedDate': null, 
  'maxCpu': 1, 
  'maxCpuUnits': 'CORE', 
  'maxMemory': 1024, 
  'metricPollDate': null, 
  'modifyDate': null, 
  'privateNetworkOnlyFlag': false, 
  'startCpus': 1, 
  'statusId': 1001, 
  'globalIdentifier': '2d203774-0ee1-49f5-9599-6ef67358dd31' 
} 
``` "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_Guest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/createObject'
```
