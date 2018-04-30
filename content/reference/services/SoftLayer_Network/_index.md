---
title: "SoftLayer_Network"
description: "A SoftLayer_Network represents a container for which subnetting is managed by the Account and not SoftLayer's automated... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
---
# SoftLayer_Network
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network' >Datatype</a></li>
    </ul>
</div>

## Description
A SoftLayer_Network represents a container for which subnetting is managed by the Account and not SoftLayer's automated network management. It provides an isolated network segment on the backend network in which a portion of RFC 1918 IP address space must be used. This feature replaces SoftLayer's automated network management on the backend network, but retains automated management on the frontend network. Thus, public IP assignment will remain dynamic and on-demand. This service and related operations are only available to Accounts with no existing network or compute resources. 

A Network consists of a root subnet specification which defines the bounds of all Subnets within the Network. Subnets created within the Network must not exceed the Network's bounds nor overlap with one another. However, multiple Networks may specify identical or overlapping root subnets. 

The following constraints apply to Network creation: 
* The Network's size must only be between CIDR /16 and /24, inclusive.
* The Network's IP address space must be within that defined by RFC 1918.
* All RFC 1918 is available, but only a subset is available per Network.
The following range of blocks are valid: 
* 192.168.0.0 - 192.168.255.0 /16 - 24
* 172.16.0.0 - 172.31.255.0 /16 - 24
* 10.0.0.0 - 10.255.255.0 /16 - 24


Management of a Network occurs entirely via the SoftLayer_Network service. This includes the addition and removal of Subnets. Subnets are required before compute resources may be provisioned. A subnet defines the portion of a Network that is available within a [[SoftLayer_Network_Pod|Pods]]. 

See [[SoftLayer_Network/createObject]] and [[SoftLayer_Network/createSubnet]]. 

### External Links


* [RFC 1918](https://tools.ietf.org/html/rfc1918)




        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a Network</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/createSubnet'> createSubnet</a> </span>
            <div class='views-field-body'>Add a Subnet to the Network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Remove the Network</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/deleteSubnet'> deleteSubnet</a> </span>
            <div class='views-field-body'>Remove a Subnet from the Network</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/editObject'> editObject</a> </span>
            <div class='views-field-body'>Modify the Network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Retrieve the Networks for your Account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getCidr'> getCidr</a> </span>
            <div class='views-field-body'>Retrieve the size of the Network specified in CIDR notation. Specified in conjunction with the ``networkIdentifier`` to describe the bounding subnet size for the Network. Required for creation. See [[SoftLayer_Network/createObject]] documentation for creation details.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getName'> getName</a> </span>
            <div class='views-field-body'>Retrieve a name for the Network. This is required during creation of a Network and is entirely user defined.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getNetworkIdentifier'> getNetworkIdentifier</a> </span>
            <div class='views-field-body'>Retrieve the starting IP address of the Network. Specified in conjunction with the ``cidr`` property to specify the bounding IP address space for the Network. Required for creation. See [[SoftLayer_Network/createObject]] documentation for creation details.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getNotes'> getNotes</a> </span>
            <div class='views-field-body'>Retrieve notes, or a description of the Network. This is entirely user defined.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network/getSubnets'> getSubnets</a> </span>
            <div class='views-field-body'>Retrieve the Subnets within the Network. These represent the realized segments of the Network and reside within a [[SoftLayer_Network_Pod|Pod]]. A Subnet must be specified when provisioning a compute resource within a Network.</div>
        </div>
        </div>
</div>

