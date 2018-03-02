---
title: "createObject"
description: "<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> 
createObject() enab... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::createObject
## Overview 

<style type="text/css">.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> 
createObject() enables the creation of computing instances on an account. This 
method is a simplified alternative to interacting with the ordering system directly. 


In order to create a computing instance, a template object must be sent in with a few required 
values. 


When this method returns an order will have been placed for a computing instance of the specified configuration. 


To determine when the instance is available you can poll the instance via [[SoftLayer_Virtual_Guest/getObject|getObject]], with an [[Extended-Object-Masks|object mask]] requesting the <code>provisionDate</code> relational property. When <code>provisionDate</code> is not null, the instance will be ready. 


<b>Warning:</b> Computing instances created via this method will incur charges on your account. For testing input parameters see [[SoftLayer_Virtual_Guest/generateOrderTemplate|generateOrderTemplate]]. 


<b>Input</b> - [[SoftLayer_Virtual_Guest (type)|SoftLayer_Virtual_Guest]] 
<ul class="create_object"> 
    <li id="guest-create-object-hostname"><code>hostname</code> 
        <div>Hostname for the computing instance.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-domain"><code>domain</code> 
        <div>Domain for the computing instance.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-start-cpus"><code>startCpus</code> 
        <div>The number of CPU cores to allocate.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - int</li> 
            <li>See [[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-max-memory"><code>maxMemory</code> 
        <div>The amount of memory to allocate in megabytes.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - int</li> 
            <li>See [[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-datacenter-name"><code>datacenter.name</code> 
        <div>Specifies which datacenter the instance is to be provisioned in.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
            <li>The <code>datacenter</code> property is a [[SoftLayer_Location (type)|location]] structure with the <code>name</code> field set.</li> 
            <li>See [[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <http title="Example">{ 
    "datacenter": { 
        "name": "dal05" 
    } 
}</http> 
        <br /> 
    </li> 
    <li  id="guest-create-object-hourly-billing-flag"><code>hourlyBillingFlag</code> 
        <div>Specifies the billing type for the instance.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - boolean</li> 
            <li>When true the computing instance will be billed on hourly usage, otherwise it will be billed on a monthly basis.</li> 
        </ul> 
        <br /> 
    </li> 
    <li  id="guest-create-object-local-disk-flag"><code>localDiskFlag</code> 
        <div>Specifies the disk type for the instance.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - boolean</li> 
            <li>When true the disks for the computing instance will be provisioned on the host which it runs, otherwise SAN disks will be provisioned.</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-dedicated-account-host-only-flag"><code>dedicatedAccountHostOnlyFlag</code> 
        <div>Specifies whether or not the instance must only run on hosts with instances from the same account</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - boolean</li> 
            <li><b>Default</b> - <code>false</code></li> 
            <li>When true this flag specifies that a compute instance is to run on hosts that only have guests from the same account.</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-operating-system-reference-code"><code>operatingSystemReferenceCode</code> 
        <div>An identifier for the operating system to provision the computing instance with.</div><ul> 
            <li><b>Conditionally required</b> - Disallowed when <code>blockDeviceTemplateGroup.globalIdentifier</code> is provided, as the template will specify the operating system.</li> 
            <li><b>Type</b> - string</li> 
            <li><b>Notice</b> - Some operating systems are charged based on the value specified in <code>startCpus</code>. The price which is used can be determined by calling [[SoftLayer_Virtual_Guest/generateOrderTemplate|generateOrderTemplate]] with your desired device specifications.</li> 
            <li>See [[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-block-device-template-group-global-identifier"><code>blockDeviceTemplateGroup.globalIdentifier</code> 
        <div>A global identifier for the template to be used to provision the computing instance.</div><ul> 
            <li><b>Conditionally required</b> - Disallowed when <code>operatingSystemReferenceCode</code> is provided, as the template will specify the operating system.</li> 
            <li><b>Type</b> - string</li> 
            <li><b>Notice</b> - Some operating systems are charged based on the value specified in <code>startCpus</code>. The price which is used can be determined by calling [[SoftLayer_Virtual_Guest/generateOrderTemplate|generateOrderTemplate]] with your desired device specifications.</li> 
            <li>Both public and non-public images may be specified.</li> 
            <li>A list of public images may be obtained via a request to [[SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicImages|getPublicImages]].</li> 
            <li>A list of non-public images, images owned by an account or specifically shared with an account, may be obtained via a request to [[SoftLayer_Account/getBlockDeviceTemplateGroups|getBlockDeviceTemplateGroups]].</li> 
        </ul> 
        <http title="Example">{ 
    "blockDeviceTemplateGroup": { 
        "globalIdentifier": "07beadaa-1e11-476e-a188-3f7795feb9fb" 
    } 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-network-components-max-speed"><code>networkComponents.maxSpeed</code> 
        <div>Specifies the connection speed for the instance's network components.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - int</li> 
            <li><b>Default</b> - 10</li> 
            <li><b>Description</b> - The <code>networkComponents</code> property is an array with a single [[SoftLayer_Virtual_Guest_Network_Component (type)|network component]] structure. The <code>maxSpeed</code> property must be set to specify the network uplink speed, in megabits per second, of the computing instance.</li> 
            <li>See [[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
            <http title="Example">{ 
    "networkComponents": [ 
        { 
            "maxSpeed": 1000 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-private-network-only-flag"><code>privateNetworkOnlyFlag</code> 
        <div>Specifies whether or not the instance only has access to the private network</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - boolean</li> 
            <li><b>Default</b> - <code>false</code></li> 
            <li>When true this flag specifies that a compute instance is to only have access to the private network.</li> 
        </ul> 
        <br /> 
    </li> 
    <li id="guest-create-object-primary-network-component-network-vlan-id"><code>primaryNetworkComponent.networkVlan.id</code> 
        <div>Specifies the network vlan which is to be used for the frontend interface of the computing instance.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - int</li> 
            <li><b>Description</b> - The <code>primaryNetworkComponent</code> property is a [[SoftLayer_Virtual_Guest_Network_Component (type)|network component]] structure with the <code>networkVlan</code> property populated with a [[SoftLayer_Network_Vlan (type)|vlan]] structure. The <code>id</code> property must be set to specify the frontend network vlan of the computing instance.</li> 
        </ul> 
        <http title="Example">{ 
    "primaryNetworkComponent": { 
        "networkVlan": { 
            "id": 1 
        } 
    } 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-primary-backend-network-component-network-vlan-id"><code>primaryBackendNetworkComponent.networkVlan.id</code> 
        <div>Specifies the network vlan which is to be used for the backend interface of the computing instance.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - int</li> 
            <li><b>Description</b> - The <code>primaryBackendNetworkComponent</code> property is a [[SoftLayer_Virtual_Guest_Network_Component (type)|network component]] structure with the <code>networkVlan</code> property populated with a [[SoftLayer_Network_Vlan (type)|vlan]] structure. The <code>id</code> property must be set to specify the backend network vlan of the computing instance.</li> 
        </ul> 
        <http title="Example">{ 
    "primaryBackendNetworkComponent": { 
        "networkVlan": { 
            "id": 2 
        } 
    } 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-primary-network-component-security-group-bindings"><code>primaryNetworkComponent.securityGroupBindings</code> 
        <div>Specifies the security groups to be attached to this VSI's Frontend Network Adapter</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - array of [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)| SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding]] with the securityGroup property set.</li> 
            <li><b>Description</b> - The <code>primaryNetworkComponent</code> property is a [[SoftLayer_Virtual_Guest_Network_Component (type)|network component]] structure with the <code>securityGroupBindings</code> property populated with an array of [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)|Security Group Order Binding]] structures. The <code>securityGroup</code> property in each must be set to specify the security group to be attached to the primary frontend network component.</li> 
        </ul> 
        <http title="Example">{ 
    "primaryNetworkComponent": { 
        "securityGroupBindings": [ 
            { 
                "securityGroup": { 
                    "id": 1 
                } 
            }, 
            { 
                "securityGroup": { 
                    "id": 2 
                } 
            } 
        ] 
    } 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-primary-backend-network-component-security-group-bindings"><code>primaryBackendNetworkComponent.securityGroupBindings</code> 
        <div>Specifies the security groups to be attached to this VSI's Backend Network Adapter</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - array of [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)| SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding]] with the securityGroup property set.</li> 
            <li><b>Description</b> - The <code>primaryBackendNetworkComponent</code> property is a [[SoftLayer_Virtual_Guest_Network_Component (type)|network component]] structure with the <code>securityGroupBindings</code> property populated with an array of [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)|Security Group Order Binding]] structures. The <code>securityGroup</code> property in each must be set to specify the security group to be attached to the primary backend network component.</li> 
        </ul> 
        <http title="Example">{ 
    "primaryBackendNetworkComponent": { 
        "securityGroupBindings": [ 
            { 
                "securityGroup": { 
                    "id": 1 
                } 
            }, 
            { 
                "securityGroup": { 
                    "id": 2 
                } 
            } 
        ] 
   } 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-block-devices"><code>blockDevices</code> 
        <div>Block device and disk image settings for the computing instance</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - array of [[SoftLayer_Virtual_Guest_Block_Device (type)|SoftLayer_Virtual_Guest_Block_Device]</li> 
            <li><b>Default</b> - The smallest available capacity for the primary disk will be used. If an image template is specified the disk capacity will be be provided by the template.</li> 
            <li><b>Description</b> - The <code>blockDevices</code> property is an array of [[SoftLayer_Virtual_Guest_Block_Device (type)|block device]] structures.</i> 
            <li>Each block device must specify the <code>device</code> property along with the <code>diskImage</code> property, which is a [[SoftLayer_Virtual_Disk_Image (type)|disk image]] structure with the <code>capacity</code> property set.</li> 
            <li>The <code>device</code> number <code>'1'</code> is reserved for the SWAP disk attached to the computing instance.</li> 
            <li>See [[SoftLayer_Virtual_Guest/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <http title="Example">{ 
    "blockDevices": [ 
        { 
            "device": "0", 
            "diskImage": { 
                "capacity": 100 
            } 
        } 
    ], 
    "localDiskFlag": true 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-user-data"><code>userData.value</code> 
        <div>Arbitrary data to be made available to the computing instance.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - string</li> 
            <li><b>Description</b> - The <code>userData</code> property is an array with a single [[SoftLayer_Virtual_Guest_Attribute (type)|attribute]] structure with the <code>value</code> property set to an arbitrary value.</li> 
            <li>This value can be retrieved via the [[SoftLayer_Resource_Metadata/getUserMetadata|getUserMetadata]] method from a request originating from the computing instance. This is primarily useful for providing data to software that may be on the instance and configured to execute upon first boot.</li> 
        </ul> 
        <http title="Example">{ 
    "userData": [ 
        { 
            "value": "someValue" 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-ssh-keys"><code>sshKeys</code> 
        <div>SSH keys to install on the computing instance upon provisioning.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - array of [[SoftLayer_Security_Ssh_Key (type)|SoftLayer_Security_Ssh_Key]]</li> 
            <li><b>Description</b> - The <code>sshKeys</code> property is an array of [[SoftLayer_Security_Ssh_Key (type)|SSH Key]] structures with the <code>id</code> property set to the value of an existing SSH key.</li> 
            <li>To create a new SSH key, call [[SoftLayer_Security_Ssh_Key/createObject|createObject]] on the [[SoftLayer_Security_Ssh_Key]] service.</li> 
            <li>To obtain a list of existing SSH keys, call [[SoftLayer_Account/getSshKeys|getSshKeys]] on the [[SoftLayer_Account]] service. 
        </ul> 
        <http title="Example">{ 
    "sshKeys": [ 
        { 
            "id": 123 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li id="guest-create-object-post-install-script-uri"><code>postInstallScriptUri</code> 
        <div>Specifies the uri location of the script to be downloaded and run after installation is complete.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - string</li> 
        </ul> 
        <br /> 
    </li> 
</ul> 


<h1>REST Example</h1> 
<http title="Request">curl -X POST -d '{ 
 "parameters":[ 
     { 
         "hostname": "host1", 
         "domain": "example.com", 
         "startCpus": 1, 
         "maxMemory": 1024, 
         "hourlyBillingFlag": true, 
         "localDiskFlag": true, 
         "operatingSystemReferenceCode": "UBUNTU_LATEST" 
     } 
 ] 
}' https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest.json 
</http> 
<http title="Response">HTTP/1.1 201 Created 
Location: https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/1301396/getObject 


{ 
    "accountId": 232298, 
    "createDate": "2012-11-30T16:28:17-06:00", 
    "dedicatedAccountHostOnlyFlag": false, 
    "domain": "example.com", 
    "hostname": "host1", 
    "id": 1301396, 
    "lastPowerStateId": null, 
    "lastVerifiedDate": null, 
    "maxCpu": 1, 
    "maxCpuUnits": "CORE", 
    "maxMemory": 1024, 
    "metricPollDate": null, 
    "modifyDate": null, 
    "privateNetworkOnlyFlag": false, 
    "startCpus": 1, 
    "statusId": 1001, 
    "globalIdentifier": "2d203774-0ee1-49f5-9599-6ef67358dd31" 
} 
</http> 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>| The SoftLayer_Virtual_Guest object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>


### associatedMethods

*  [SoftLayer_Virtual_Guest::createObjects](/reference/services/SoftLayer_Virtual_Guest/createObjects )
*  [SoftLayer_Virtual_Guest::generateOrderTemplate](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate )
*  [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions )

