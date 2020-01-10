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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[cosAccountId]: #cosaccountid
#### [cosAccountId]
The account id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[cosBucket]: #cosbucket
#### [cosBucket]
The Cloud Object Storage bucket.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[eth1Gateway]: #eth1gateway
#### [eth1Gateway]
The eth1 gateway for connecting to private network in datacenter.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[eth1IpAddress]: #eth1ipaddress
#### [eth1IpAddress]
The eth1 IP address for connecting to private network in datacenter.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[eth1Netmask]: #eth1netmask
#### [eth1Netmask]
The eth1 netmask for connecting to private network in datacenter.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[eth3Gateway]: #eth3gateway
#### [eth3Gateway]
The eth3 gateway for connecting to private network at customer's location.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[eth3IpAddress]: #eth3ipaddress
#### [eth3IpAddress]
The eth3 IP address for connecting to private network at customer location.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[eth3Netmask]: #eth3netmask
#### [eth3Netmask]
The eth3 netmask for connecting to private network in at customer's location.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique id of the request status.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
The password for configuring network share.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[poolLockPassword]: #poollockpassword
#### [poolLockPassword]
The pool lock password for configuring network share.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[requestId]: #requestid
#### [requestId]
The request id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[s3Url]: #s3url
#### [s3Url]
The Cloud Object Storage bucket URL.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[shareName]: #sharename
#### [shareName]
The name of network share.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
The username for configuring network share.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[request]: #request
#### [request]
The request this device configurations belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request'>SoftLayer_Network_Storage_MassDataMigration_Request </a>**


</div>
<div class="prop-row">

-----
[storageAccount]: #storageaccount
#### [storageAccount]
The storage account to use for this request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Hub_Cleversafe_Account'>SoftLayer_Network_Storage_Hub_Cleversafe_Account </a>**


</div>

## Count
</div>


