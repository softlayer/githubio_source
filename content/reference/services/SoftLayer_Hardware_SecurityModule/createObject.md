---
title: "createObject"
description: "
<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> 
createObject() enables the creation of servers on an account. This 
method is a simplified alternative to interacting with the ordering system directly. 


In order to create a server, a template object must be sent in with a few required 
values. 


When this method returns an order will have been placed for a server of the specified configuration. 


To determine when the server is available you can poll the server via [[SoftLayer_Hardware/getObject|getObject]], 
checking the <code>provisionDate</code> property. 
When <code>provisionDate</code> is not null, the server will be ready. Be sure to use the <code>globalIdentifier</code> 
as your initialization parameter. 


<b>Warning:</b> Servers created via this method will incur charges on your account. For testing input parameters see [[SoftLayer_Hardware/generateOrderTemplate|generateOrderTemplate]]. 


<b>Input</b> - [[SoftLayer_Hardware (type)|SoftLayer_Hardware]] 
<ul class='create_object'> 
    <li><code>hostname</code> 
        <div>Hostname for the server.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>domain</code> 
        <div>Domain for the server.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>processorCoreAmount</code> 
        <div>The number of logical CPU cores to allocate.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - int</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>memoryCapacity</code> 
        <div>The amount of memory to allocate in gigabytes.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - int</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>hourlyBillingFlag</code> 
        <div>Specifies the billing type for the server.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - boolean</li> 
            <li>When true the server will be billed on hourly usage, otherwise it will be billed on a monthly basis.</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>operatingSystemReferenceCode</code> 
        <div>An identifier for the operating system to provision the server with.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>datacenter.name</code> 
        <div>Specifies which datacenter the server is to be provisioned in.</div><ul> 
            <li><b>Required</b></li> 
            <li><b>Type</b> - string</li> 
            <li>The <code>datacenter</code> property is a [[SoftLayer_Location (type)|location]] structure with the <code>name</code> field set.</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <http title='Example'>{ 
    'datacenter': { 
        'name': 'dal05' 
    } 
}</http> 
        <br /> 
    </li> 
    <li><code>networkComponents.maxSpeed</code> 
        <div>Specifies the connection speed for the server's network components.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - int</li> 
            <li><b>Default</b> - The highest available zero cost port speed will be used.</li> 
            <li><b>Description</b> - The <code>networkComponents</code> property is an array with a single [[SoftLayer_Network_Component (type)|network component]] structure. The <code>maxSpeed</code> property must be set to specify the network uplink speed, in megabits per second, of the server.</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
            <http title='Example'>{ 
    'networkComponents': [ 
        { 
            'maxSpeed': 1000 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li><code>networkComponents.redundancyEnabledFlag</code> 
        <div>Specifies whether or not the server's network components should be in redundancy groups.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - bool</li> 
            <li><b>Default</b> - <code>false</code></li> 
            <li><b>Description</b> - The <code>networkComponents</code> property is an array with a single [[SoftLayer_Network_Component (type)|network component]] structure. When the <code>redundancyEnabledFlag</code> property is true the server's network components will be in redundancy groups.</li> 
        </ul> 
            <http title='Example'>{ 
    'networkComponents': [ 
        { 
            'redundancyEnabledFlag': false 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li><code>privateNetworkOnlyFlag</code> 
        <div>Specifies whether or not the server only has access to the private network</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - boolean</li> 
            <li><b>Default</b> - <code>false</code></li> 
            <li>When true this flag specifies that a server is to only have access to the private network.</li> 
        </ul> 
        <br /> 
    </li> 
    <li><code>primaryNetworkComponent.networkVlan.id</code> 
        <div>Specifies the network vlan which is to be used for the frontend interface of the server.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - int</li> 
            <li><b>Description</b> - The <code>primaryNetworkComponent</code> property is a [[SoftLayer_Network_Component (type)|network component]] structure with the <code>networkVlan</code> property populated with a [[SoftLayer_Network_Vlan (type)|vlan]] structure. The <code>id</code> property must be set to specify the frontend network vlan of the server.</li> 
        </ul> 
        <http title='Example'>{ 
    'primaryNetworkComponent': { 
        'networkVlan': { 
            'id': 1 
        } 
    } 
}</http> 
        <br /> 
    </li> 
    <li><code>primaryBackendNetworkComponent.networkVlan.id</code> 
        <div>Specifies the network vlan which is to be used for the backend interface of the server.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - int</li> 
            <li><b>Description</b> - The <code>primaryBackendNetworkComponent</code> property is a [[SoftLayer_Network_Component (type)|network component]] structure with the <code>networkVlan</code> property populated with a [[SoftLayer_Network_Vlan (type)|vlan]] structure. The <code>id</code> property must be set to specify the backend network vlan of the server.</li> 
        </ul> 
        <http title='Example'>{ 
    'primaryBackendNetworkComponent': { 
        'networkVlan': { 
            'id': 2 
        } 
    } 
}</http> 
        <br /> 
    </li> 
    <li><code>fixedConfigurationPreset.keyName</code> 
        <div></div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - string</li> 
            <li><b>Description</b> - The <code>fixedConfigurationPreset</code> property is a [[SoftLayer_Product_Package_Preset (type)|fixed configuration preset]] structure. The <code>keyName</code> property must be set to specify preset to use.</li> 
            <li>If a fixed configuration preset is used <code>processorCoreAmount</code>, <code>memoryCapacity</code> and <code>hardDrives</code> properties must not be set.</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <http title='Example'>{ 
    'fixedConfigurationPreset': { 
        'keyName': 'SOME_KEY_NAME' 
    } 
}</http> 
        <br /> 
    </li> 
    <li><code>userData.value</code> 
        <div>Arbitrary data to be made available to the server.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - string</li> 
            <li><b>Description</b> - The <code>userData</code> property is an array with a single [[SoftLayer_Hardware_Attribute (type)|attribute]] structure with the <code>value</code> property set to an arbitrary value.</li> 
            <li>This value can be retrieved via the [[SoftLayer_Resource_Metadata/getUserMetadata|getUserMetadata]] method from a request originating from the server. This is primarily useful for providing data to software that may be on the server and configured to execute upon first boot.</li> 
        </ul> 
        <http title='Example'>{ 
    'userData': [ 
        { 
            'value': 'someValue' 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li><code>hardDrives</code> 
        <div>Hard drive settings for the server</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - SoftLayer_Hardware_Component</li> 
            <li><b>Default</b> - The largest available capacity for a zero cost primary disk will be used.</li> 
            <li><b>Description</b> - The <code>hardDrives</code> property is an array of [[SoftLayer_Hardware_Component (type)|hardware component]] structures.</i> 
            <li>Each hard drive must specify the <code>capacity</code> property.</li> 
            <li>See [[SoftLayer_Hardware/getCreateObjectOptions|getCreateObjectOptions]] for available options.</li> 
        </ul> 
        <http title='Example'>{ 
    'hardDrives': [ 
        { 
            'capacity': 500 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li id='hardware-create-object-ssh-keys'><code>sshKeys</code> 
        <div>SSH keys to install on the server upon provisioning.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - array of [[SoftLayer_Security_Ssh_Key (type)|SoftLayer_Security_Ssh_Key]]</li> 
            <li><b>Description</b> - The <code>sshKeys</code> property is an array of [[SoftLayer_Security_Ssh_Key (type)|SSH Key]] structures with the <code>id</code> property set to the value of an existing SSH key.</li> 
            <li>To create a new SSH key, call [[SoftLayer_Security_Ssh_Key/createObject|createObject]] on the [[SoftLayer_Security_Ssh_Key]] service.</li> 
            <li>To obtain a list of existing SSH keys, call [[SoftLayer_Account/getSshKeys|getSshKeys]] on the [[SoftLayer_Account]] service. 
        </ul> 
        <http title='Example'>{ 
    'sshKeys': [ 
        { 
            'id': 123 
        } 
    ] 
}</http> 
        <br /> 
    </li> 
    <li><code>postInstallScriptUri</code> 
        <div>Specifies the uri location of the script to be downloaded and run after installation is complete.</div><ul> 
            <li><b>Optional</b></li> 
            <li><b>Type</b> - string</li> 
        </ul> 
        <br /> 
    </li> 
</ul> 


<h1>REST Example</h1> 
<http title='Request'>curl -X POST -d '{ 
 'parameters':[ 
     { 
         'hostname': 'host1', 
         'domain': 'example.com', 
         'processorCoreAmount': 2, 
         'memoryCapacity': 2, 
         'hourlyBillingFlag': true, 
         'operatingSystemReferenceCode': 'UBUNTU_LATEST' 
     } 
 ] 
}' https://api.softlayer.com/rest/v3/SoftLayer_Hardware.json 
</http> 
<http title='Response'>HTTP/1.1 201 Created 
Location: https://api.softlayer.com/rest/v3/SoftLayer_Hardware/f5a3fcff-db1d-4b7c-9fa0-0349e41c29c5/getObject 


{ 
    'accountId': 232298, 
    'bareMetalInstanceFlag': null, 
    'domain': 'example.com', 
    'hardwareStatusId': null, 
    'hostname': 'host1', 
    'id': null, 
    'serviceProviderId': null, 
    'serviceProviderResourceId': null, 
    'globalIdentifier': 'f5a3fcff-db1d-4b7c-9fa0-0349e41c29c5', 
    'hourlyBillingFlag': true, 
    'memoryCapacity': 2, 
    'operatingSystemReferenceCode': 'UBUNTU_LATEST', 
    'processorCoreAmount': 2 
} 
</http> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "createObject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---
