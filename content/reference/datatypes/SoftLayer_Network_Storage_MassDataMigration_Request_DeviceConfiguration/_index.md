---
title: "SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration"
description: "The SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration data type contains settings such networking,... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration"
---

# SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration data type contains settings such networking, COS account, which needs to be configured on device for a Mass Data Migration Request. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[cosAccountId]: #cosaccountid
#### [cosAccountId]
The account id.  
<span class="type-label">Type: </span>**integer**

-----
[cosBucket]: #cosbucket
#### [cosBucket]
The Cloud Object Storage bucket.  
<span class="type-label">Type: </span>**string**

-----
[eth1Gateway]: #eth1gateway
#### [eth1Gateway]
The eth1 gateway for connecting to private network in datacenter.  
<span class="type-label">Type: </span>**string**

-----
[eth1IpAddress]: #eth1ipaddress
#### [eth1IpAddress]
The eth1 IP address for connecting to private network in datacenter.  
<span class="type-label">Type: </span>**string**

-----
[eth1Netmask]: #eth1netmask
#### [eth1Netmask]
The eth1 netmask for connecting to private network in datacenter.  
<span class="type-label">Type: </span>**string**

-----
[eth3Gateway]: #eth3gateway
#### [eth3Gateway]
The eth3 gateway for connecting to private network at customer's location.  
<span class="type-label">Type: </span>**string**

-----
[eth3IpAddress]: #eth3ipaddress
#### [eth3IpAddress]
The eth3 IP address for connecting to private network at customer location.  
<span class="type-label">Type: </span>**string**

-----
[eth3Netmask]: #eth3netmask
#### [eth3Netmask]
The eth3 netmask for connecting to private network in at customer's location.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique id of the request status.  
<span class="type-label">Type: </span>**integer**

-----
[password]: #password
#### [password]
The password for configuring network share.  
<span class="type-label">Type: </span>**string**

-----
[poolLockPassword]: #poollockpassword
#### [poolLockPassword]
The pool lock password for configuring network share.  
<span class="type-label">Type: </span>**string**

-----
[requestId]: #requestid
#### [requestId]
The request id.  
<span class="type-label">Type: </span>**integer**

-----
[s3Url]: #s3url
#### [s3Url]
The Cloud Object Storage bucket URL.  
<span class="type-label">Type: </span>**string**

-----
[shareName]: #sharename
#### [shareName]
The name of network share.  
<span class="type-label">Type: </span>**string**

-----
[username]: #username
#### [username]
The username for configuring network share.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[request]: #request
#### [request]
The request this device configurations belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request'>SoftLayer_Network_Storage_MassDataMigration_Request </a>**

-----
[storageAccount]: #storageaccount
#### [storageAccount]
The storage account to use for this request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Hub_Cleversafe_Account'>SoftLayer_Network_Storage_Hub_Cleversafe_Account </a>**


## Count
</div>


