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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cosAccountId" name=cosAccountId>cosAccountId</a></span>
            <div class='views-field-body'>The account id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cosBucket" name=cosBucket>cosBucket</a></span>
            <div class='views-field-body'>The Cloud Object Storage bucket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eth1Gateway" name=eth1Gateway>eth1Gateway</a></span>
            <div class='views-field-body'>The eth1 gateway for connecting to private network in datacenter. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eth1IpAddress" name=eth1IpAddress>eth1IpAddress</a></span>
            <div class='views-field-body'>The eth1 IP address for connecting to private network in datacenter. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eth1Netmask" name=eth1Netmask>eth1Netmask</a></span>
            <div class='views-field-body'>The eth1 netmask for connecting to private network in datacenter. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eth3Gateway" name=eth3Gateway>eth3Gateway</a></span>
            <div class='views-field-body'>The eth3 gateway for connecting to private network at customer's location. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eth3IpAddress" name=eth3IpAddress>eth3IpAddress</a></span>
            <div class='views-field-body'>The eth3 IP address for connecting to private network at customer location. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eth3Netmask" name=eth3Netmask>eth3Netmask</a></span>
            <div class='views-field-body'>The eth3 netmask for connecting to private network in at customer's location. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique id of the request status. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#password" name=password>password</a></span>
            <div class='views-field-body'>The password for configuring network share. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#poolLockPassword" name=poolLockPassword>poolLockPassword</a></span>
            <div class='views-field-body'>The pool lock password for configuring network share. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#requestId" name=requestId>requestId</a></span>
            <div class='views-field-body'>The request id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shareName" name=shareName>shareName</a></span>
            <div class='views-field-body'>The name of network share. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#username" name=username>username</a></span>
            <div class='views-field-body'>The username for configuring network share. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#request" name=request>request</a></span>
            <div class='views-field-body'>The request this device configurations belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request'>SoftLayer_Network_Storage_MassDataMigration_Request </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#storageAccount" name=storageAccount>storageAccount</a></span>
            <div class='views-field-body'>The storage account to use for this request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage_Hub_Cleversafe_Account'>SoftLayer_Network_Storage_Hub_Cleversafe_Account </a></p></div>
        </div>
            </div>
</div>


